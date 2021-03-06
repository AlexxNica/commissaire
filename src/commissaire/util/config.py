# Copyright (C) 2016  Red Hat, Inc
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
Configuration related classes.
"""

import importlib
import json
import logging
import os
import os.path
import sys

import etcd

from urllib.parse import urlparse

from commissaire import constants as C
from commissaire.errors import CommissaireError
from commissaire.util.logging import setup_logging


class ConfigurationError(CommissaireError):
    """
    Exception class for user configuration errors.
    """
    pass


def _normalize_member_names(json_object):
    """
    Normalize member names by converting hyphens to underscores.

    :param json_object: Dictionary to normalize.
    :type json_object: dict
    :returns: A normalized dictionary.
    :rtype: dict
    """
    normalized = {}
    for k, v in json_object.items():
        k = k.replace('-', '_')
        if isinstance(v, dict):
            v = _normalize_member_names(v)
        normalized[k] = v
    return normalized


def etcd_client_args():
    """
    Assembles a keyword argument dictionary from environment variables,
    suitable for passing to ``etcd.Client``.

    The environment variables used are:

    ``ETCD_MACHINES`` - comma-separated list of etcd service URLs
    ``ETCD_TLSPEM`` - path of TLS client certificate - public key
    ``ETCD_TLSKEY`` - path of TLS client certificate - private key
    ``ETCD_CACERT`` - path of TLS certificate authority public key
    ``ETCD_USERNAME`` - username used for basic auth
    ``ETCD_PASSWORD`` - password used for basic auth
    """
    args = {
        'cert': None,  # see below
        'ca_cert': os.environ.get('ETCD_CACERT'),
        'username': os.environ.get('ETCD_USERNAME'),
        'password': os.environ.get('ETCD_PASSWORD')
    }

    try:
        args['cert'] = (
            os.environ['ETCD_TLSPEM'],
            os.environ['ETCD_TLSKEY'])
    except KeyError:
        pass

    try:
        for string in os.environ['ETCD_MACHINES'].split(','):
            url = urlparse(string, scheme='http')
            host_port = (url.hostname, url.port)
            args.setdefault('host', []).append(host_port)

            # XXX URL schemes should all be identical,
            #     but first one wins in any case.
            args.setdefault('protocol', url.scheme)

        # etcd.Client expects 'host' to be a tuple or string,
        # so convert our list of tuples to a tuple of tuples.
        if 'host' in args:
            args['host'] = tuple(args['host'])
            # Required when 'host' is a tuple.
            args['allow_reconnect'] = True
    except KeyError:
        pass

    return args


def _read_etcd_config_key(key, json_object):
    """
    Tries to read from etcd as described in read_config_file().
    """
    # Log relevant environment variables.
    # We know we have at least ETCD_MACHINES.
    def maybe_print_environ(key, secret=False):
        if key in os.environ:
            value = '(redacted)' if secret else repr(os.environ[key])
            print('  {}={}'.format(key, value))
        else:
            print('  {} not defined'.format(key))
    print('Environment variables:')
    maybe_print_environ('ETCD_MACHINES')
    maybe_print_environ('ETCD_TLSPEM')
    maybe_print_environ('ETCD_TLSKEY')
    maybe_print_environ('ETCD_CACERT')
    maybe_print_environ('ETCD_USERNAME')
    maybe_print_environ('ETCD_PASSWORD', secret=True)

    try:
        client = etcd.Client(**etcd_client_args())
        json_object.update(json.loads(client.get(key).value))
        print('Using configuration in etcd at "{}"'.format(key))
    except etcd.EtcdConnectionFailed as error:
        print(
            'Connection to etcd failed: {}'.format(error.args[0]),
            file=sys.stderr)
    except etcd.EtcdKeyNotFound:
        print(
            'Missing etcd configuration key "{}"'.format(key),
            file=sys.stderr)
    except json.JSONDecodeError as error:
        print(
            'Skipping invalid configuration in etcd key "{}": {}'.format(
                key, error.args[0]), file=sys.stderr)
    except (TypeError, ValueError):
        print(
            'Skipping invalid configuration in etcd key "{}": {}'.format(
                key, 'Content must be a JSON object'), file=sys.stderr)


def read_config_file(path=None, default=C.DEFAULT_CONFIGURATION_FILE):
    """
    Attempts to parse configuration data, formatted as a JSON object.

    This first tries to read configuration from etcd, if an environment
    variable named ``ETCD_MACHINES`` is defined (a comma-delimited list
    of URLs).  The etcd key is derived from the basename of the default
    configuration file (e.g. for ``/path/to/storage.conf`` the etcd key
    would be ``/commissaire/config/storage``).

    Failing that, the function then tries to read a local config file.

    If a config file path is explicitly given, then failure to open the
    file will raise an IOError.  Otherwise a default path is tried, but
    no IOError is raised on failure.  If the file can be opened but not
    parsed, an exception is always raised.

    :param path: Full path to the config file, or None
    :type path: str or None
    :param default: The default file path to user
    :type default: str
    :returns: configuration content as a dictionary
    :rtype: dict
    :raises: IOError, TypeError, ValueError
    """
    json_object = {}
    using_default = False

    if 'ETCD_MACHINES' in os.environ:
        # Derive etcd key from the default file path.
        basename = os.path.basename(default).split('.', 1)[0]
        key = '/commissaire/config/' + basename
        _read_etcd_config_key(key, json_object)

    if not json_object:
        # As with the fileinput module, replace '-' with sys.stdin.
        if path == '-':
            json_object = json.load(sys.stdin)

        else:
            if path is None:
                path = default
                using_default = True

            try:
                with open(path, 'r') as fp:
                    json_object = json.load(fp)
                if using_default:
                    print('Using configuration in {}'.format(path))
            except IOError:
                if not using_default:
                    raise

        if not isinstance(json_object, dict):
            raise TypeError(
                '{}: File content must be a JSON object'.format(path))

    # Recursively normalize the JSON member names.
    json_object = _normalize_member_names(json_object)

    # Process any logging configuration straight away.
    # This is NOT included in the returned dictionary.
    if 'logging' in json_object:
        setup_logging(json_object.pop('logging'))

    # Handle the debug log-level option straight away.
    # This is NOT included in the returned dictionary.
    if json_object.pop('debug', False):
        logging.getLogger().setLevel(logging.DEBUG)
        logging.info('Debugging messages enabled')

    # Special case:
    #
    # In the configuration file, the "authentication_plugins" member
    # can also be specified as a list of JSON objects.  Each object must
    # have at least a 'name' member specifying the plugin module name.
    auth_plugins = json_object.get('authentication_plugins', [])
    configured_plugins = {}

    if auth_plugins and not isinstance(auth_plugins, list):
        raise ValueError(
            '{}: "{}" must be a list. Not at {}.'.format(
                path, auth_plugins, type(auth_plugins)))

    for plugin in auth_plugins:
        if isinstance(plugin, dict):
            if 'name' not in plugin.keys():
                raise ValueError(
                    '{}: "{}" is missing a "name" member'.format(
                        path, plugin))
            # Since it's valid we can parse it down into the
            # expected format for loading.
            configured_plugins[plugin.pop('name')] = plugin

    # Overwrite authentication_plugins with the configured_plugins
    json_object['authentication_plugins'] = configured_plugins

    # Special case:
    #
    # In the configuration file, the "storage_handlers" member can
    # be specified as a JSON object or a list of JSON objects.
    handler_key = 'storage_handlers'
    handler_list = json_object.get(handler_key)
    if isinstance(handler_list, dict):
        json_object[handler_key] = [handler_list]

    return json_object


def import_plugin(module_name, default_package, base_class):
    """
    Imports a user-specified module and returns its "PluginClass"
    attribute, which should be a subclass of the given base class.

    If module_name lacks a module delimiter character ('.'), then use
    default_package as the prefix to obtain the absolute module name.

    :param module_name: Module name to import
    :type module_name: str
    :param default_package: Default if module_name lacks a package
    :type package_name: str
    :param base_class: Required base class of the imported plugin
    :type base_class: class
    :returns: A plugin class
    :rtype: class
    :raises ConfigurationError: if the module_name is invalid, the
                                "PluginClass" attribute is not defined,
                                or the imported object is not a subclass
                                of base_class
    """
    if '.' not in module_name:
        module_name = default_package + '.' + module_name
    try:
        module = importlib.import_module(module_name)
        plugin_class = getattr(module, 'PluginClass')
        if not issubclass(plugin_class, base_class):
            raise ConfigurationError(
                '{}.PluginClass is not a subclass of {}'.format(
                    module_name, base_class.__name__))
        return plugin_class
    except (AttributeError, ImportError, TypeError) as error:
        raise ConfigurationError(error.args[0])
