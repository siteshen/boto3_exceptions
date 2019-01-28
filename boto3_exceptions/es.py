import boto3

exceptions = boto3.client('es').exceptions

BaseException = exceptions.BaseException
DisabledOperationException = exceptions.DisabledOperationException
InternalException = exceptions.InternalException
InvalidTypeException = exceptions.InvalidTypeException
LimitExceededException = exceptions.LimitExceededException
ResourceAlreadyExistsException = exceptions.ResourceAlreadyExistsException
ResourceNotFoundException = exceptions.ResourceNotFoundException
ValidationException = exceptions.ValidationException
