import boto3

exceptions = boto3.client('sms-voice').exceptions

AlreadyExistsException = exceptions.AlreadyExistsException
BadRequestException = exceptions.BadRequestException
InternalServiceErrorException = exceptions.InternalServiceErrorException
LimitExceededException = exceptions.LimitExceededException
NotFoundException = exceptions.NotFoundException
TooManyRequestsException = exceptions.TooManyRequestsException
