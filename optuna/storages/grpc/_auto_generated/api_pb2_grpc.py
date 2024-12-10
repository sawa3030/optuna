# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import optuna.storages.grpc._auto_generated.api_pb2 as api__pb2

GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in api_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class StorageServiceStub(object):
    """*
    Optuna storage service defines APIs to interact with the storage.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateNewStudy = channel.unary_unary(
                '/optuna.StorageService/CreateNewStudy',
                request_serializer=api__pb2.CreateNewStudyRequest.SerializeToString,
                response_deserializer=api__pb2.CreateNewStudyReply.FromString,
                _registered_method=True)
        self.DeleteStudy = channel.unary_unary(
                '/optuna.StorageService/DeleteStudy',
                request_serializer=api__pb2.DeleteStudyRequest.SerializeToString,
                response_deserializer=api__pb2.DeleteStudyReply.FromString,
                _registered_method=True)
        self.SetStudyUserAttribute = channel.unary_unary(
                '/optuna.StorageService/SetStudyUserAttribute',
                request_serializer=api__pb2.SetStudyUserAttributeRequest.SerializeToString,
                response_deserializer=api__pb2.SetStudyUserAttributeReply.FromString,
                _registered_method=True)
        self.SetStudySystemAttribute = channel.unary_unary(
                '/optuna.StorageService/SetStudySystemAttribute',
                request_serializer=api__pb2.SetStudySystemAttributeRequest.SerializeToString,
                response_deserializer=api__pb2.SetStudySystemAttributeReply.FromString,
                _registered_method=True)
        self.GetStudyIdFromName = channel.unary_unary(
                '/optuna.StorageService/GetStudyIdFromName',
                request_serializer=api__pb2.GetStudyIdFromNameRequest.SerializeToString,
                response_deserializer=api__pb2.GetStudyIdFromNameReply.FromString,
                _registered_method=True)
        self.GetStudyNameFromId = channel.unary_unary(
                '/optuna.StorageService/GetStudyNameFromId',
                request_serializer=api__pb2.GetStudyNameFromIdRequest.SerializeToString,
                response_deserializer=api__pb2.GetStudyNameFromIdReply.FromString,
                _registered_method=True)
        self.GetStudyDirections = channel.unary_unary(
                '/optuna.StorageService/GetStudyDirections',
                request_serializer=api__pb2.GetStudyDirectionsRequest.SerializeToString,
                response_deserializer=api__pb2.GetStudyDirectionsReply.FromString,
                _registered_method=True)
        self.GetStudyUserAttributes = channel.unary_unary(
                '/optuna.StorageService/GetStudyUserAttributes',
                request_serializer=api__pb2.GetStudyUserAttributesRequest.SerializeToString,
                response_deserializer=api__pb2.GetStudyUserAttributesReply.FromString,
                _registered_method=True)
        self.GetStudySystemAttributes = channel.unary_unary(
                '/optuna.StorageService/GetStudySystemAttributes',
                request_serializer=api__pb2.GetStudySystemAttributesRequest.SerializeToString,
                response_deserializer=api__pb2.GetStudySystemAttributesReply.FromString,
                _registered_method=True)
        self.GetAllStudies = channel.unary_unary(
                '/optuna.StorageService/GetAllStudies',
                request_serializer=api__pb2.GetAllStudiesRequest.SerializeToString,
                response_deserializer=api__pb2.GetAllStudiesReply.FromString,
                _registered_method=True)
        self.CreateNewTrial = channel.unary_unary(
                '/optuna.StorageService/CreateNewTrial',
                request_serializer=api__pb2.CreateNewTrialRequest.SerializeToString,
                response_deserializer=api__pb2.CreateNewTrialReply.FromString,
                _registered_method=True)
        self.SetTrialParameter = channel.unary_unary(
                '/optuna.StorageService/SetTrialParameter',
                request_serializer=api__pb2.SetTrialParameterRequest.SerializeToString,
                response_deserializer=api__pb2.SetTrialParameterReply.FromString,
                _registered_method=True)
        self.GetTrialIdFromStudyIdTrialNumber = channel.unary_unary(
                '/optuna.StorageService/GetTrialIdFromStudyIdTrialNumber',
                request_serializer=api__pb2.GetTrialIdFromStudyIdTrialNumberRequest.SerializeToString,
                response_deserializer=api__pb2.GetTrialIdFromStudyIdTrialNumberReply.FromString,
                _registered_method=True)
        self.SetTrialStateValues = channel.unary_unary(
                '/optuna.StorageService/SetTrialStateValues',
                request_serializer=api__pb2.SetTrialStateValuesRequest.SerializeToString,
                response_deserializer=api__pb2.SetTrialStateValuesReply.FromString,
                _registered_method=True)
        self.SetTrialIntermediateValue = channel.unary_unary(
                '/optuna.StorageService/SetTrialIntermediateValue',
                request_serializer=api__pb2.SetTrialIntermediateValueRequest.SerializeToString,
                response_deserializer=api__pb2.SetTrialIntermediateValueReply.FromString,
                _registered_method=True)
        self.SetTrialUserAttribute = channel.unary_unary(
                '/optuna.StorageService/SetTrialUserAttribute',
                request_serializer=api__pb2.SetTrialUserAttributeRequest.SerializeToString,
                response_deserializer=api__pb2.SetTrialUserAttributeReply.FromString,
                _registered_method=True)
        self.SetTrialSystemAttribute = channel.unary_unary(
                '/optuna.StorageService/SetTrialSystemAttribute',
                request_serializer=api__pb2.SetTrialSystemAttributeRequest.SerializeToString,
                response_deserializer=api__pb2.SetTrialSystemAttributeReply.FromString,
                _registered_method=True)
        self.GetTrial = channel.unary_unary(
                '/optuna.StorageService/GetTrial',
                request_serializer=api__pb2.GetTrialRequest.SerializeToString,
                response_deserializer=api__pb2.GetTrialReply.FromString,
                _registered_method=True)
        self.GetAllTrials = channel.unary_unary(
                '/optuna.StorageService/GetAllTrials',
                request_serializer=api__pb2.GetAllTrialsRequest.SerializeToString,
                response_deserializer=api__pb2.GetAllTrialsReply.FromString,
                _registered_method=True)


class StorageServiceServicer(object):
    """*
    Optuna storage service defines APIs to interact with the storage.
    """

    def CreateNewStudy(self, request, context):
        """*
        Create a new study.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteStudy(self, request, context):
        """*
        Delete a study.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetStudyUserAttribute(self, request, context):
        """*
        Set a study's user attribute.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetStudySystemAttribute(self, request, context):
        """*
        Set a study's system attribute.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStudyIdFromName(self, request, context):
        """*
        Get a study id by its name.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStudyNameFromId(self, request, context):
        """*
        Get a study name by its id.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStudyDirections(self, request, context):
        """*
        Get study directions.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStudyUserAttributes(self, request, context):
        """*
        Get study user attributes.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStudySystemAttributes(self, request, context):
        """*
        Get study system attributes.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllStudies(self, request, context):
        """*
        Get all studies.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateNewTrial(self, request, context):
        """*
        Create a new trial.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetTrialParameter(self, request, context):
        """*
        Set a trial parameter.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTrialIdFromStudyIdTrialNumber(self, request, context):
        """*
        Get a trial id from its study id and trial number.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetTrialStateValues(self, request, context):
        """*
        Set trial state and values. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetTrialIntermediateValue(self, request, context):
        """*
        Set a trial intermediate value. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetTrialUserAttribute(self, request, context):
        """*
        Set a trial user attribute.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetTrialSystemAttribute(self, request, context):
        """*
        Set a trial system attribute.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTrial(self, request, context):
        """*
        Get a trial by its ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllTrials(self, request, context):
        """*
        Get all trials in a study.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StorageServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateNewStudy': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateNewStudy,
                    request_deserializer=api__pb2.CreateNewStudyRequest.FromString,
                    response_serializer=api__pb2.CreateNewStudyReply.SerializeToString,
            ),
            'DeleteStudy': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteStudy,
                    request_deserializer=api__pb2.DeleteStudyRequest.FromString,
                    response_serializer=api__pb2.DeleteStudyReply.SerializeToString,
            ),
            'SetStudyUserAttribute': grpc.unary_unary_rpc_method_handler(
                    servicer.SetStudyUserAttribute,
                    request_deserializer=api__pb2.SetStudyUserAttributeRequest.FromString,
                    response_serializer=api__pb2.SetStudyUserAttributeReply.SerializeToString,
            ),
            'SetStudySystemAttribute': grpc.unary_unary_rpc_method_handler(
                    servicer.SetStudySystemAttribute,
                    request_deserializer=api__pb2.SetStudySystemAttributeRequest.FromString,
                    response_serializer=api__pb2.SetStudySystemAttributeReply.SerializeToString,
            ),
            'GetStudyIdFromName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStudyIdFromName,
                    request_deserializer=api__pb2.GetStudyIdFromNameRequest.FromString,
                    response_serializer=api__pb2.GetStudyIdFromNameReply.SerializeToString,
            ),
            'GetStudyNameFromId': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStudyNameFromId,
                    request_deserializer=api__pb2.GetStudyNameFromIdRequest.FromString,
                    response_serializer=api__pb2.GetStudyNameFromIdReply.SerializeToString,
            ),
            'GetStudyDirections': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStudyDirections,
                    request_deserializer=api__pb2.GetStudyDirectionsRequest.FromString,
                    response_serializer=api__pb2.GetStudyDirectionsReply.SerializeToString,
            ),
            'GetStudyUserAttributes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStudyUserAttributes,
                    request_deserializer=api__pb2.GetStudyUserAttributesRequest.FromString,
                    response_serializer=api__pb2.GetStudyUserAttributesReply.SerializeToString,
            ),
            'GetStudySystemAttributes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStudySystemAttributes,
                    request_deserializer=api__pb2.GetStudySystemAttributesRequest.FromString,
                    response_serializer=api__pb2.GetStudySystemAttributesReply.SerializeToString,
            ),
            'GetAllStudies': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllStudies,
                    request_deserializer=api__pb2.GetAllStudiesRequest.FromString,
                    response_serializer=api__pb2.GetAllStudiesReply.SerializeToString,
            ),
            'CreateNewTrial': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateNewTrial,
                    request_deserializer=api__pb2.CreateNewTrialRequest.FromString,
                    response_serializer=api__pb2.CreateNewTrialReply.SerializeToString,
            ),
            'SetTrialParameter': grpc.unary_unary_rpc_method_handler(
                    servicer.SetTrialParameter,
                    request_deserializer=api__pb2.SetTrialParameterRequest.FromString,
                    response_serializer=api__pb2.SetTrialParameterReply.SerializeToString,
            ),
            'GetTrialIdFromStudyIdTrialNumber': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTrialIdFromStudyIdTrialNumber,
                    request_deserializer=api__pb2.GetTrialIdFromStudyIdTrialNumberRequest.FromString,
                    response_serializer=api__pb2.GetTrialIdFromStudyIdTrialNumberReply.SerializeToString,
            ),
            'SetTrialStateValues': grpc.unary_unary_rpc_method_handler(
                    servicer.SetTrialStateValues,
                    request_deserializer=api__pb2.SetTrialStateValuesRequest.FromString,
                    response_serializer=api__pb2.SetTrialStateValuesReply.SerializeToString,
            ),
            'SetTrialIntermediateValue': grpc.unary_unary_rpc_method_handler(
                    servicer.SetTrialIntermediateValue,
                    request_deserializer=api__pb2.SetTrialIntermediateValueRequest.FromString,
                    response_serializer=api__pb2.SetTrialIntermediateValueReply.SerializeToString,
            ),
            'SetTrialUserAttribute': grpc.unary_unary_rpc_method_handler(
                    servicer.SetTrialUserAttribute,
                    request_deserializer=api__pb2.SetTrialUserAttributeRequest.FromString,
                    response_serializer=api__pb2.SetTrialUserAttributeReply.SerializeToString,
            ),
            'SetTrialSystemAttribute': grpc.unary_unary_rpc_method_handler(
                    servicer.SetTrialSystemAttribute,
                    request_deserializer=api__pb2.SetTrialSystemAttributeRequest.FromString,
                    response_serializer=api__pb2.SetTrialSystemAttributeReply.SerializeToString,
            ),
            'GetTrial': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTrial,
                    request_deserializer=api__pb2.GetTrialRequest.FromString,
                    response_serializer=api__pb2.GetTrialReply.SerializeToString,
            ),
            'GetAllTrials': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllTrials,
                    request_deserializer=api__pb2.GetAllTrialsRequest.FromString,
                    response_serializer=api__pb2.GetAllTrialsReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'optuna.StorageService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('optuna.StorageService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class StorageService(object):
    """*
    Optuna storage service defines APIs to interact with the storage.
    """

    @staticmethod
    def CreateNewStudy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/optuna.StorageService/CreateNewStudy',
            api__pb2.CreateNewStudyRequest.SerializeToString,
            api__pb2.CreateNewStudyReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteStudy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/optuna.StorageService/DeleteStudy',
            api__pb2.DeleteStudyRequest.SerializeToString,
            api__pb2.DeleteStudyReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SetStudyUserAttribute(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/optuna.StorageService/SetStudyUserAttribute',
            api__pb2.SetStudyUserAttributeRequest.SerializeToString,
            api__pb2.SetStudyUserAttributeReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SetStudySystemAttribute(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/optuna.StorageService/SetStudySystemAttribute',
            api__pb2.SetStudySystemAttributeRequest.SerializeToString,
            api__pb2.SetStudySystemAttributeReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetStudyIdFromName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/optuna.StorageService/GetStudyIdFromName',
            api__pb2.GetStudyIdFromNameRequest.SerializeToString,
            api__pb2.GetStudyIdFromNameReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetStudyNameFromId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/optuna.StorageService/GetStudyNameFromId',
            api__pb2.GetStudyNameFromIdRequest.SerializeToString,
            api__pb2.GetStudyNameFromIdReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetStudyDirections(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/optuna.StorageService/GetStudyDirections',
            api__pb2.GetStudyDirectionsRequest.SerializeToString,
            api__pb2.GetStudyDirectionsReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetStudyUserAttributes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/optuna.StorageService/GetStudyUserAttributes',
            api__pb2.GetStudyUserAttributesRequest.SerializeToString,
            api__pb2.GetStudyUserAttributesReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetStudySystemAttributes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/optuna.StorageService/GetStudySystemAttributes',
            api__pb2.GetStudySystemAttributesRequest.SerializeToString,
            api__pb2.GetStudySystemAttributesReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetAllStudies(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/optuna.StorageService/GetAllStudies',
            api__pb2.GetAllStudiesRequest.SerializeToString,
            api__pb2.GetAllStudiesReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CreateNewTrial(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/optuna.StorageService/CreateNewTrial',
            api__pb2.CreateNewTrialRequest.SerializeToString,
            api__pb2.CreateNewTrialReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SetTrialParameter(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/optuna.StorageService/SetTrialParameter',
            api__pb2.SetTrialParameterRequest.SerializeToString,
            api__pb2.SetTrialParameterReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetTrialIdFromStudyIdTrialNumber(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/optuna.StorageService/GetTrialIdFromStudyIdTrialNumber',
            api__pb2.GetTrialIdFromStudyIdTrialNumberRequest.SerializeToString,
            api__pb2.GetTrialIdFromStudyIdTrialNumberReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SetTrialStateValues(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/optuna.StorageService/SetTrialStateValues',
            api__pb2.SetTrialStateValuesRequest.SerializeToString,
            api__pb2.SetTrialStateValuesReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SetTrialIntermediateValue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/optuna.StorageService/SetTrialIntermediateValue',
            api__pb2.SetTrialIntermediateValueRequest.SerializeToString,
            api__pb2.SetTrialIntermediateValueReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SetTrialUserAttribute(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/optuna.StorageService/SetTrialUserAttribute',
            api__pb2.SetTrialUserAttributeRequest.SerializeToString,
            api__pb2.SetTrialUserAttributeReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SetTrialSystemAttribute(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/optuna.StorageService/SetTrialSystemAttribute',
            api__pb2.SetTrialSystemAttributeRequest.SerializeToString,
            api__pb2.SetTrialSystemAttributeReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetTrial(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/optuna.StorageService/GetTrial',
            api__pb2.GetTrialRequest.SerializeToString,
            api__pb2.GetTrialReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetAllTrials(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/optuna.StorageService/GetAllTrials',
            api__pb2.GetAllTrialsRequest.SerializeToString,
            api__pb2.GetAllTrialsReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
