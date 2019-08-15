import boto3

exceptions = boto3.client('athena').exceptions

InternalServerException = exceptions.InternalServerException
InvalidRequestException = exceptions.InvalidRequestException
ResourceNotFoundException = exceptions.ResourceNotFoundException
TooManyRequestsException = exceptions.TooManyRequestsException
