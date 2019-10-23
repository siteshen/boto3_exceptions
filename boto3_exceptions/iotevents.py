import boto3

exceptions = boto3.client('iotevents').exceptions

InternalFailureException = exceptions.InternalFailureException
InvalidRequestException = exceptions.InvalidRequestException
LimitExceededException = exceptions.LimitExceededException
ResourceAlreadyExistsException = exceptions.ResourceAlreadyExistsException
ResourceInUseException = exceptions.ResourceInUseException
ResourceNotFoundException = exceptions.ResourceNotFoundException
ServiceUnavailableException = exceptions.ServiceUnavailableException
ThrottlingException = exceptions.ThrottlingException
UnsupportedOperationException = exceptions.UnsupportedOperationException