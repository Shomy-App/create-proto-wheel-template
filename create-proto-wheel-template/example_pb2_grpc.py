# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import example_pb2 as example__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class ExampleStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getData = channel.unary_unary(
                '/examplePackage.Example/getData',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=example__pb2.dataResponse.FromString,
                )
        self.createData = channel.unary_unary(
                '/examplePackage.Example/createData',
                request_serializer=example__pb2.dataRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class ExampleServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def createData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ExampleServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getData': grpc.unary_unary_rpc_method_handler(
                    servicer.getData,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=example__pb2.dataResponse.SerializeToString,
            ),
            'createData': grpc.unary_unary_rpc_method_handler(
                    servicer.createData,
                    request_deserializer=example__pb2.dataRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'examplePackage.Example', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Example(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/examplePackage.Example/getData',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            example__pb2.dataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def createData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/examplePackage.Example/createData',
            example__pb2.dataRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)