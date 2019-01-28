import boto3

exceptions = boto3.client('fms').exceptions

InternalErrorException = exceptions.InternalErrorException
InvalidInputException = exceptions.InvalidInputException
InvalidOperationException = exceptions.InvalidOperationException
InvalidTypeException = exceptions.InvalidTypeException
LimitExceededException = exceptions.LimitExceededException
ResourceNotFoundException = exceptions.ResourceNotFoundException
