import boto3

exceptions = boto3.client('rds-data').exceptions

BadRequestException = exceptions.BadRequestException
ForbiddenException = exceptions.ForbiddenException
InternalServerErrorException = exceptions.InternalServerErrorException
NotFoundException = exceptions.NotFoundException
ServiceUnavailableError = exceptions.ServiceUnavailableError
StatementTimeoutException = exceptions.StatementTimeoutException
