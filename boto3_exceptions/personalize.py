import boto3

exceptions = boto3.client('personalize').exceptions

InvalidInputException = exceptions.InvalidInputException
InvalidNextTokenException = exceptions.InvalidNextTokenException
LimitExceededException = exceptions.LimitExceededException
ResourceAlreadyExistsException = exceptions.ResourceAlreadyExistsException
ResourceInUseException = exceptions.ResourceInUseException
ResourceNotFoundException = exceptions.ResourceNotFoundException
