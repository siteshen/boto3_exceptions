import boto3

exceptions = boto3.client('cloud9').exceptions

BadRequestException = exceptions.BadRequestException
ConflictException = exceptions.ConflictException
ForbiddenException = exceptions.ForbiddenException
InternalServerErrorException = exceptions.InternalServerErrorException
LimitExceededException = exceptions.LimitExceededException
NotFoundException = exceptions.NotFoundException
TooManyRequestsException = exceptions.TooManyRequestsException
