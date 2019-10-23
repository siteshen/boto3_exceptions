import boto3

exceptions = boto3.client('forecastquery').exceptions

InvalidInputException = exceptions.InvalidInputException
InvalidNextTokenException = exceptions.InvalidNextTokenException
LimitExceededException = exceptions.LimitExceededException
ResourceInUseException = exceptions.ResourceInUseException
ResourceNotFoundException = exceptions.ResourceNotFoundException
