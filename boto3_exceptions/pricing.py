import boto3

exceptions = boto3.client('pricing').exceptions

ExpiredNextTokenException = exceptions.ExpiredNextTokenException
InternalErrorException = exceptions.InternalErrorException
InvalidNextTokenException = exceptions.InvalidNextTokenException
InvalidParameterException = exceptions.InvalidParameterException
NotFoundException = exceptions.NotFoundException
