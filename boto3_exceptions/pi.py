import boto3

exceptions = boto3.client('pi').exceptions

InternalServiceError = exceptions.InternalServiceError
InvalidArgumentException = exceptions.InvalidArgumentException
NotAuthorizedException = exceptions.NotAuthorizedException
