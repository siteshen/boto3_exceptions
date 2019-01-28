import boto3

exceptions = boto3.client('medialive').exceptions

BadGatewayException = exceptions.BadGatewayException
BadRequestException = exceptions.BadRequestException
ConflictException = exceptions.ConflictException
ForbiddenException = exceptions.ForbiddenException
GatewayTimeoutException = exceptions.GatewayTimeoutException
InternalServerErrorException = exceptions.InternalServerErrorException
NotFoundException = exceptions.NotFoundException
TooManyRequestsException = exceptions.TooManyRequestsException
UnprocessableEntityException = exceptions.UnprocessableEntityException
