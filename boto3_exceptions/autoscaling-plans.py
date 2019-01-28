import boto3

exceptions = boto3.client('autoscaling-plans').exceptions

ConcurrentUpdateException = exceptions.ConcurrentUpdateException
InternalServiceException = exceptions.InternalServiceException
InvalidNextTokenException = exceptions.InvalidNextTokenException
LimitExceededException = exceptions.LimitExceededException
ObjectNotFoundException = exceptions.ObjectNotFoundException
ValidationException = exceptions.ValidationException
