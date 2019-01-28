import boto3

exceptions = boto3.client('cloudhsm').exceptions

CloudHsmInternalException = exceptions.CloudHsmInternalException
CloudHsmServiceException = exceptions.CloudHsmServiceException
InvalidRequestException = exceptions.InvalidRequestException
