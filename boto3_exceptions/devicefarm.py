import boto3

exceptions = boto3.client('devicefarm').exceptions

ArgumentException = exceptions.ArgumentException
IdempotencyException = exceptions.IdempotencyException
InvalidOperationException = exceptions.InvalidOperationException
LimitExceededException = exceptions.LimitExceededException
NotEligibleException = exceptions.NotEligibleException
NotFoundException = exceptions.NotFoundException
ServiceAccountException = exceptions.ServiceAccountException
