import boto3

exceptions = boto3.client('cloudhsmv2').exceptions

CloudHsmAccessDeniedException = exceptions.CloudHsmAccessDeniedException
CloudHsmInternalFailureException = exceptions.CloudHsmInternalFailureException
CloudHsmInvalidRequestException = exceptions.CloudHsmInvalidRequestException
CloudHsmResourceNotFoundException = exceptions.CloudHsmResourceNotFoundException
CloudHsmServiceException = exceptions.CloudHsmServiceException
