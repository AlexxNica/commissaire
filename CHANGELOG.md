# commissaire v0.0.6
```
* de14431: tox.ini: Fix command for "bdd" test environment.
* 9cf24e5: bdd-requirements.txt: Remove disabled lines.
* 5c4d859: Don't require commctl in test environments.
* 5117b9c: tox.ini: Add "-D start-custodia" to behave command.
* af38936: e2e: Update for Custodia integration.
* 1e6fe49: Deal with custodia directory in etcd.
* f461ee2: Vagrantfile: Simplify custodia authentication.
* 57401a3: Vagrantfile: Use the custodia pip package instead of rpm.
* 1d277f8: Test model class attribute invariants.
* 2109ba4: models: Add SecretModel._key_container attribute.
* f1d34e3: storage: Remove unused StoreHandlerBase._get_connection().
* 378d671: util: Add UnixAdapter from requests-unixsocket.
* 329c9e1: storage: Merge Host and HostCreds models into same etcd key.
* f695855: Vagrantfile: Install custodia on commissaire host.
* e3550e5: Vagrantfile: Readability cleanups.
* bf8b8ad: Move vagrant data files to their own subdir.
* 87eb249: util: TemporarySSHKey now uses HostCreds
* 963f6fa: models: Add secret model per cpd-101
* efe8c42: models: Add _must_be_in for validation
* 9f1d83c: Post-release version bump.
```

# commissaire v0.0.5
```
* b94e6f7: doc: Update community meeting time.
* c1ba64b: doc: Document how to fetch configuration from etcd.
* 33e5a40: etcd: Use environment variables as a default config.
* fdc4fe8: util: Support reading configuration from etcd.
* cad1c86: test: Add tests for NotifyCallback.
* f28bf4a: Vagrantfile: Disable "self-auths" in commissaire-server.
* 00018f4: storage: The notification event is 'updated', not 'changed'.
* 2febdc3: doc: Talk about StorageClient and notifications.
* 30f18ec: doc: Remove docs for StoreHandlerManager.
* fa45a0c: Vagrantfile: Disable watcher service.
* 9c1bfd9: e2e: Verify storage notifications in steps.
* 6c5ff90: storage: Add NotifyCallback decorator.
* 4e53b46: storage: Add StorageClient.get_consumers().
* ab65248: storage: Add StorageClient.register_callback().
* 0436064: storage: Add StorageNotify class.
* 4b315ff: Post-release version bump.
```

# commissaire v0.0.4
```
* 1bc1444: docs: Add Tuomas Kuosmanen to CONTRIBUTORS
* 29123b3: doc: Add self-auth example
* 972affd: doc: Marking cpd-101 as accepted
* 0683116: doc: Added CPD-101 documentation
* 7413a93: doc: Fix CPD-61 version.
* cf6cc73: doc: Update for commctl user-data command
* 774686a: tools: Remove cloud-init files
* 959865e: doc: Add generation of user-data help file
* c6581c5: doc: Added walkthrough
* 0002687: doc: Minor clarifications
* 6dd6561: constants: Add DEFAULT_CONFIGURATION_FILE.
* c534d64: Note for ZSH users
* 7c2c1a7: Fix up some small mistakes
* 62ff811: Update devel instructions formatting
* ea7e9df: Fix link to DEVEL instructions in RTD sources.
* d3f91ca: logging: Switch to lazy string formatting
* c5482df: models: Remove to_dict_with_hosts().
* e05ca2b: models: Add expose arg to to_dict(), to_dict_safe().
* 505d629: models: Remove to_json_with_hosts().
* 23e84f9: Post-release version bump.
```

# commissaire v0.0.3
```
* db92fb8: doc: Fix cluster DELETE header.
* 88849c6: models: to_list_safe() called but does not exist.
* 5b03fa5: storage: Clarify the list() method is only for ListModels.
* e735f92: models: Add ListModel.
* 1f6ec9c: doc: Added apidocs for errors and containermgr.trivial
* 819414c: e2e: Update STORAGE_CONF_TEMPLATE.
* ce2e047: doc: Document Host.source field.
* a20aed9: docs: Commit generated docs for commissaire.containermgr.Trivial.
* 66f7191: docs: Commit generated docs for commissaire.errors.
* 92b4735: e2e: Use new host status constants.
* 993bb41: e2e: Verify host status after waiting for bootstrap.
* 03bc051: e2e: Test host status with a container manager.
* af35ee7: e2e: Distinguish clusters with no container manager.
* 23cc340: containermgr: Add TrivialContainerManager for testing.
* dae5c10: constants: Add HOST_STATUS_DISASSOCIATED.
* 4e3f8b1: constants: Added host statuses.
* d0e69d4: doc: Removed inactive from enums
* 433bd39: doc: Added website to README
* 3605213: doc: Added release information
* afe5a32: doc: Update community meeting time for DST in US
* b919bf3: Add 'METHOD_NOT_ALLOWED' to JSONRPC_ERRORS.
* 348e9dc: storage: Added get_uniform_model_type
* d5508c3: StorageClient: Add get_many(), save_many(), delete_many().
* e017998: models: to_json* now can expose internal attributes
* 96dcbf0: String formats now using implicit reference
* f845b4f: models: Primary key attribute should not have default.
* cbb29b7: container: Dockerfile now using COPY rather than ADD
* 44ceb6f: bus: Remove old formatting style in exception
* c35c51e: errors: Exceptions bound by a hierarchy.
* 486b502: doc: Updated bdd examples.
* 095017a: Make ContainerManagerError inherit from RemoteProcedureCallError.
* 39c6e52: Simplify super() calls.
* a72da6d: Post-release version bump.
```

# commissaire v0.0.2
```
* d92fafd: tools: Added script to generate changelog
* eeafc34: doc: Clean up for 0.0.2
* d324816: doc: Stop adding TODOs in output HTML
* 46cd1f0: doc: Add new intro to overview
* fcc6739: doc: Remove containerhandlermanager docs
* e119d1c: README.md: Improve Commissaire's introduction.
* 9da6c1a: containermgr: Implement remove_all_nodes() for Kubernetes.
* 4689cb3: containermgr: Add method stubs to ContainerManagerBase.
* 3859ad7: containermgr: Added openshift which is an alias to kubernetes
* 2c9e121: doc: Update "Authentication Plugins" page.
* b072c51: e2e: Now works on travis.
* bd526c2: constants: Remove DEFAULT_KUBERNETES_STORE_HANDLER.
* f07aaa8: config: Add import_plugin function.
* cd129e9: e2e: Tag clusterexec test cases as @slow.
* fca7580: e2e: Generate config for commissaire-storage-service.
* d1190ef: e2e: Remove unused 'times' param from try_start().
* 7a35c72: config: Allow reading configuration from standard input.
* cf4dac3: e2e: Specify config file for each backend service.
* d7860fa: e2e: Fix typo in host create test case.
* 6e0ae35: config: Log an acknowledgement when enabling debug messages.
* 22b5e88: Registered ContainerManagerConfig model.
* 162b04c: container: Added VOLUME for data.
* 7b337dc: container: Minor updates to Dockerfile.
* c331b47: container: Added VOLUME for configuration.
* fc4df83: container: Added Dockerfile and startup-all-in-one.sh
* 0e3f843: bug: Updated network constant to include options.
* ffba214: Moved community meetings to Tuesday.
* ec3448d: constants: Add 'NOT_FOUND' to JSONRPC_ERRORS.
* 33bd77d: Vagrantfile: Adapt to new location of etcd_init.sh.
* 7abe930: Vagrantfile: Fix etcd configuration.
* 7c44777: Bus: Raise StorageLookupError from JSON-RPC message
* 0c94e4d: Add StorageLookupError.
* dfff387: constants: Fix typo in JSONRPC_ERRORS.
* 11865aa: constants: Added CLUSTER_STATUS_*.
* 4bb36fc: Removed dead status code.
* 8f1781d: doc: Update configuration file details for services.
* 3306b20: util: Simplify logging configuration.
* e37df86: e2e: Remove dummy feature.
* 9b8cd0c: e2e: Cleanup old format code.
* c20831a: models: str understands list and dict models.
* b3d3090: e2e: Fixed ssl_server typo.
* 8a3a75e: Vagrantfile: Have etcd listen on all interfaces.
* f747236: e2e: Creating a compatible host returns 201
* 3c6441b: e2e: Create etcd dirs as part of test suite setup
* c08d86a: tools: Add etcd_init.sh.
* ac16a91: e2e: Fixed BUS_URI to use redis.
* ce7577c: e2e: client cert server now runs.
* 4c78697: vagrant: No longer doing upgrade on atomic.
* a89217f: docs: Vagrant docs use vagrantup and denote the right OS versions.
* f4c8fd5: tools: Added vagrantup.
* 88c42dd: vagrant: Services now listen on all interfaces.
* 2710e22: e2e: Changes to get behave tests to at least run.
* 9c91fdb: e2e: Import behave tests from commissaire-mvp.
* bd8735d: config: Added default to read_config_file.
* ecae028: doc: Removed etcd logging docs.
* fda025b: doc: Added example configuration for storage service.
* 38e34fb: doc: componenets now references services for docs.
* 9b14a26: doc: Added basic commissaire-containermgr-service information.
* 84ca57b: Kubernetes container handler (#68)
* 0fd8209: Vagrantfile updates (#67)
* 9b3cf0f: ContainerManagerService updates. (#66)
* bf72644: Add StorageClient class (#63)
* 0a8bebc: Multiple Model Enhancements (#65)
* 49f382f: doc: Marking cpd-61 as accepted.
* db119f9: Host Data From External Systems (#62)
* 67e6591: doc: Added CPD documentation. (#60)
* 5f236f1: models: Drop 'secure' arg from to_json() and to_dict().
* e68577e: models: Add to_dict_safe() method.
* d0a3d7e: models: Add to_json_safe() method.
* 808372a: doc: Regenerated apidocs.
* c60a70d: util: Added date helper functions. (#57)
* 8e3cf4f: Dictionary keys() sometimes needs to be a list.
* 2c3fa9e: ContainerManagerConfig Model (#50)
* 09ef995: doc: Added apidocs for commissaire.util.logging.
* d49cf8e: util: Added docstrings and tests to util.logging.
* fcc0552: flake8: Fixed issue in containermgr.kubernetes.
* 6960f10: bug: Model._validate no longer updates signature. (#52)
* e9c401e: Introduce common logging utils
* 6ffba14: Update Vagrant development env from MVP to current master branches
* 7b9d256: bug: Model._validate no longer updates signature.
* d980ead: doc: Noted deprecation of bare Cluster creation.
* 11ff180: models: Validation for ClusterRestart and ClusterUpgrade. (#49)
* 8d35826: models: Added extra validation for ClusterDeploy. (#48)
* 99adb87: doc: Added community meeting information. (#47)
* ab207f3: vagrant: Ported Vagrantfile from MVP. (#41)
* 6a9ae8a: doc: Initial server config docs.
* 887347b: docs: multiple small style tweaks (#46)
* febc6dc: README: fix urls to other commissaire projects
* 22c44e5: Merge pull request #43 from ashcrow/doc-flow
* 2361ac5: doc: Updated flow diagram.
* 2eb6ff5: test: Updated bdd doc and requirements.
* 6eecea6: config: Type checking and formatting updates.
* 9dc078f: doc: Examples now use authentication-plugins in config.
* 5eadb7b: config: Multiple authentication plugin support.
* c1ef613: util: Moved normalize_member_names to full function.
* e853084: Merge pull request #38 from ashcrow/authn-doc-update
* 28edecb: Add tox instructions for commissaire-http
* 3593c08: doc: Added advanced authn plugin example.
* cb0cbe2: doc: Updated bdd examples and doc.
* bbf8f08: test: Updated tools/behave for new options.
* 2d99047: test: Ported behave environment from MVP.
* c258606: test: Limit to py35 env in .redhat-ci.yml
* df8e60d: test: Added bdd env to tox.
* aebc3b9: MANIFEST.in: Typo fix for tools directory.
* 1975c17: README.md: Misc updates
* 0ff9989: Add WatcherRecord (#36)
* c5ac3d6: config: Recursively normalize JSON object members.
* 87faa74: Merge pull request #33 from ashcrow/doc-cluster
* 0a2607a: Add Notification Support (#34)
* cdea27b: docs: Added Pete Birley to CONTRIBUTORS.
* 62b3eaf: Two changes to etcd handling: (#28)
* 9a9051b: doc: Added delete to cluster docs.
* 7e2bfef: build: Multiple requirements enhancements. (#31)
* e2fd4c1: Miscellaneous tweaks.
* d0b726b: docs: Added todos.
* 4e3a56d: docs: Updated cloud-init with new location in tools.
* 126d125: tools: Moved in the cloud-init code.
* 411bf57: docs: Update authentication_devel to current state.
* 8f80b00: docs: Added Gerard Braad to CONTRIBUTORS.
* 898b6c4: Fix typo in README.md.
* 1d8e6e3: Fix typo in INSTALL.md.
* bf36149: Development install instructions
* b9cb64d: Add information about related projects
* 299dc5c: doc: Updated host endpoint documentation.
* d3e8849: bug: EtcdStoreHandler must provide config to super.
* fa16235: Handle Unserializable etcd Responses in _list (#22)
* 0bb5df2: Update model type validation (#21)
* 776f9b6: doc: Updated network endpoint documentation.
* 3949174: doc: Updated cluster endpoint documentation.
* 1322804: doc: Added commissaire_http.constants submodule.
* cb61b7e: .redhat-ci.yml: switch to native Docker support
* c233500: models: Cluster now has added to_dict_with_hosts. (#17)
* d39106d: test: Updates to enable redhat-ci.
* b935bc2: test: Added nose-htmloutput to test requirements.
* ad40bf1: constants: Added CONFLICT to jsonrpc errors.
* b53618a: Added jsonrpc error codes to constants. (#14)
* 7864981: models: Support pre-validation.
* 11c18e8: BusMixin: Add RemoteProcedureCallException.
* 3da1cef: BusMixin: Allow implicit method name in request()
* e940e9f: models: added to_dict which wraps to_json. (#11)
* 81dff91: doc: Updates for new commissaire-http cli code. (#8)
* 39c34ff: config: read_config_file now returns the proper auth structure.
* 2a9fbca: Add util.ssh module for TemporarySSHKey.
* 24aef87: Rename config module to util.config.
* 23e85ae: bus: Added loading of messages.
* b5480f8: doc: Updated and added to apidocs. (#6)
* 017b3c1: config: Ported initial config module.
* b5d40a3: bus: Created commissaire.bus.BusMixin.
* a95d1bd: flake8: Fixed flake8 issues.
* 173f1ed: test: Fixed base test code.
* 1a2fef5: doc: Added a comment for multi-repo apidoc generation in gendocs.sh.
* 7b071bb: doc: Updated authentication devel docs.
* b18f78f: doc: Added commissaire-http docs.
* 0a9817f: doc: Removed old compat references in development.
* deea016: doc: Moved service docs over from commissaire-service.
* 6809c9c: doc: gendocs now build apidoc of subpackages if available.
* 061bd9e: Add storage handler plugins. (#3)
* e128152: test: Added travis and tox files.
* 708a926: Added in constants, containermgr and models from MVP.
```
