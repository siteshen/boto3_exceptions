import boto3

exceptions = boto3.client('rds-data').exceptions

ForbiddenException = exceptions.ForbiddenException
BadRequestException = exceptions.BadRequestException
ServiceUnavailableError = exceptions.ServiceUnavailableError
InternalServerErrorException = exceptions.InternalServerErrorException
