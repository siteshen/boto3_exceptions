import boto3

exceptions = boto3.client('apigateway').exceptions

BadRequestException = exceptions.BadRequestException
ConflictException = exceptions.ConflictException
LimitExceededException = exceptions.LimitExceededException
NotFoundException = exceptions.NotFoundException
ServiceUnavailableException = exceptions.ServiceUnavailableException
TooManyRequestsException = exceptions.TooManyRequestsException
UnauthorizedException = exceptions.UnauthorizedException
