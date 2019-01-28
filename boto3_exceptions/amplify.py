import boto3

exceptions = boto3.client('amplify').exceptions

BadRequestException = exceptions.BadRequestException
DependentServiceFailureException = exceptions.DependentServiceFailureException
InternalFailureException = exceptions.InternalFailureException
LimitExceededException = exceptions.LimitExceededException
NotFoundException = exceptions.NotFoundException
UnauthorizedException = exceptions.UnauthorizedException
