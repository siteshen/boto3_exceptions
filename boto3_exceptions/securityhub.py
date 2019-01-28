import boto3

exceptions = boto3.client('securityhub').exceptions

InternalException = exceptions.InternalException
InvalidInputException = exceptions.InvalidInputException
LimitExceededException = exceptions.LimitExceededException
ResourceNotFoundException = exceptions.ResourceNotFoundException
