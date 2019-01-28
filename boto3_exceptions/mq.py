import boto3

exceptions = boto3.client('mq').exceptions

BadRequestException = exceptions.BadRequestException
ConflictException = exceptions.ConflictException
ForbiddenException = exceptions.ForbiddenException
InternalServerErrorException = exceptions.InternalServerErrorException
NotFoundException = exceptions.NotFoundException
UnauthorizedException = exceptions.UnauthorizedException
