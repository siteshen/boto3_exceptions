import boto3

exceptions = boto3.client('securityhub').exceptions

AccessDeniedException = exceptions.AccessDeniedException
InternalException = exceptions.InternalException
InvalidAccessException = exceptions.InvalidAccessException
InvalidInputException = exceptions.InvalidInputException
LimitExceededException = exceptions.LimitExceededException
ResourceConflictException = exceptions.ResourceConflictException
ResourceNotFoundException = exceptions.ResourceNotFoundException
