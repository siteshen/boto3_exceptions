import boto3

exceptions = boto3.client('qldb-session').exceptions

BadRequestException = exceptions.BadRequestException
InvalidSessionException = exceptions.InvalidSessionException
LimitExceededException = exceptions.LimitExceededException
OccConflictException = exceptions.OccConflictException
RateExceededException = exceptions.RateExceededException
