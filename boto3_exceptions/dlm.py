import boto3

exceptions = boto3.client('dlm').exceptions

InternalServerException = exceptions.InternalServerException
InvalidRequestException = exceptions.InvalidRequestException
LimitExceededException = exceptions.LimitExceededException
ResourceNotFoundException = exceptions.ResourceNotFoundException
