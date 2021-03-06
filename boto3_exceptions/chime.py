import boto3

exceptions = boto3.client('chime').exceptions

BadRequestException = exceptions.BadRequestException
ConflictException = exceptions.ConflictException
ForbiddenException = exceptions.ForbiddenException
NotFoundException = exceptions.NotFoundException
ResourceLimitExceededException = exceptions.ResourceLimitExceededException
ServiceFailureException = exceptions.ServiceFailureException
ServiceUnavailableException = exceptions.ServiceUnavailableException
ThrottledClientException = exceptions.ThrottledClientException
UnauthorizedClientException = exceptions.UnauthorizedClientException
UnprocessableEntityException = exceptions.UnprocessableEntityException
