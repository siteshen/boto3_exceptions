import boto3

exceptions = boto3.client('iotthingsgraph').exceptions

InternalFailureException = exceptions.InternalFailureException
InvalidRequestException = exceptions.InvalidRequestException
LimitExceededException = exceptions.LimitExceededException
ResourceAlreadyExistsException = exceptions.ResourceAlreadyExistsException
ResourceInUseException = exceptions.ResourceInUseException
ResourceNotFoundException = exceptions.ResourceNotFoundException
ThrottlingException = exceptions.ThrottlingException
