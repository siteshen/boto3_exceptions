import boto3

exceptions = boto3.client('lex-models').exceptions

BadRequestException = exceptions.BadRequestException
ConflictException = exceptions.ConflictException
InternalFailureException = exceptions.InternalFailureException
LimitExceededException = exceptions.LimitExceededException
NotFoundException = exceptions.NotFoundException
PreconditionFailedException = exceptions.PreconditionFailedException
ResourceInUseException = exceptions.ResourceInUseException
