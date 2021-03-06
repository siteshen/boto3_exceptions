import boto3

exceptions = boto3.client('mediapackage-vod').exceptions

ForbiddenException = exceptions.ForbiddenException
InternalServerErrorException = exceptions.InternalServerErrorException
NotFoundException = exceptions.NotFoundException
ServiceUnavailableException = exceptions.ServiceUnavailableException
TooManyRequestsException = exceptions.TooManyRequestsException
UnprocessableEntityException = exceptions.UnprocessableEntityException
