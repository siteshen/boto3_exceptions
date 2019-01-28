import boto3

exceptions = boto3.client('signer').exceptions

AccessDeniedException = exceptions.AccessDeniedException
InternalServiceErrorException = exceptions.InternalServiceErrorException
ResourceNotFoundException = exceptions.ResourceNotFoundException
ThrottlingException = exceptions.ThrottlingException
ValidationException = exceptions.ValidationException
