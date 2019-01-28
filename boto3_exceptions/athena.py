import boto3

exceptions = boto3.client('athena').exceptions

InternalServerException = exceptions.InternalServerException
InvalidRequestException = exceptions.InvalidRequestException
TooManyRequestsException = exceptions.TooManyRequestsException
