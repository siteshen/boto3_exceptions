import boto3

exceptions = boto3.client('resource-groups').exceptions

BadRequestException = exceptions.BadRequestException
ForbiddenException = exceptions.ForbiddenException
InternalServerErrorException = exceptions.InternalServerErrorException
MethodNotAllowedException = exceptions.MethodNotAllowedException
NotFoundException = exceptions.NotFoundException
TooManyRequestsException = exceptions.TooManyRequestsException
UnauthorizedException = exceptions.UnauthorizedException
