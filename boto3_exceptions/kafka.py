import boto3

exceptions = boto3.client('kafka').exceptions

BadRequestException = exceptions.BadRequestException
ConflictException = exceptions.ConflictException
ForbiddenException = exceptions.ForbiddenException
InternalServerErrorException = exceptions.InternalServerErrorException
NotFoundException = exceptions.NotFoundException
ServiceUnavailableException = exceptions.ServiceUnavailableException
TooManyRequestsException = exceptions.TooManyRequestsException
UnauthorizedException = exceptions.UnauthorizedException
