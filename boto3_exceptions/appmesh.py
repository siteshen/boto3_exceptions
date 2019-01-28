import boto3

exceptions = boto3.client('appmesh').exceptions

InternalServerErrorException = exceptions.InternalServerErrorException
ForbiddenException = exceptions.ForbiddenException
ConflictException = exceptions.ConflictException
LimitExceededException = exceptions.LimitExceededException
TooManyRequestsException = exceptions.TooManyRequestsException
NotFoundException = exceptions.NotFoundException
ServiceUnavailableException = exceptions.ServiceUnavailableException
ResourceInUseException = exceptions.ResourceInUseException
BadRequestException = exceptions.BadRequestException
