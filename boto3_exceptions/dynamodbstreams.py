import boto3

exceptions = boto3.client('dynamodbstreams').exceptions

ExpiredIteratorException = exceptions.ExpiredIteratorException
InternalServerError = exceptions.InternalServerError
LimitExceededException = exceptions.LimitExceededException
ResourceNotFoundException = exceptions.ResourceNotFoundException
TrimmedDataAccessException = exceptions.TrimmedDataAccessException
