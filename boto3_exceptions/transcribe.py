import boto3

exceptions = boto3.client('transcribe').exceptions

BadRequestException = exceptions.BadRequestException
ConflictException = exceptions.ConflictException
InternalFailureException = exceptions.InternalFailureException
LimitExceededException = exceptions.LimitExceededException
NotFoundException = exceptions.NotFoundException
