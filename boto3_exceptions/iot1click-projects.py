import boto3

exceptions = boto3.client('iot1click-projects').exceptions

InternalFailureException = exceptions.InternalFailureException
InvalidRequestException = exceptions.InvalidRequestException
ResourceConflictException = exceptions.ResourceConflictException
ResourceNotFoundException = exceptions.ResourceNotFoundException
TooManyRequestsException = exceptions.TooManyRequestsException
