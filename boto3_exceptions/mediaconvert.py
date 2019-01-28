import boto3

exceptions = boto3.client('mediaconvert').exceptions

BadRequestException = exceptions.BadRequestException
ConflictException = exceptions.ConflictException
ForbiddenException = exceptions.ForbiddenException
InternalServerErrorException = exceptions.InternalServerErrorException
NotFoundException = exceptions.NotFoundException
TooManyRequestsException = exceptions.TooManyRequestsException
