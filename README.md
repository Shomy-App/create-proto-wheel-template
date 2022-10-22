# Proto Wheel Template
This respository has the purpose to help with the creation
of proto packages.

### Things to consider:
- The proto package take the repository name to create the wheel package, for this the repository has to be created with a valid python package name, for example:
    - myprotopackage
    - my_proto_package
- Currently the version of the package is not created automatically so you should change the version in setup.py file or your new release is going to replace the old wheel package in the dist folder.
