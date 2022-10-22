echo $PACKAGE_NAME
mkdir $PACKAGE_NAME
touch $PACKAGE_NAME/__init__.py
python -m grpc_tools.protoc --proto_path=. --python_out=$PACKAGE_NAME --grpc_python_out=$PACKAGE_NAME *.proto
