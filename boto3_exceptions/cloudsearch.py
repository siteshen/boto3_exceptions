import boto3

exceptions = boto3.client('cloudsearch').exceptions

BaseException = exceptions.BaseException
DisabledOperationException = exceptions.DisabledOperationException
InternalException = exceptions.InternalException
InvalidTypeException = exceptions.InvalidTypeException
LimitExceededException = exceptions.LimitExceededException
ResourceNotFoundException = exceptions.ResourceNotFoundException
