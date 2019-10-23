import boto3

exceptions = boto3.client('application-insights').exceptions

BadRequestException = exceptions.BadRequestException
InternalServerException = exceptions.InternalServerException
ResourceInUseException = exceptions.ResourceInUseException
ResourceNotFoundException = exceptions.ResourceNotFoundException
ValidationException = exceptions.ValidationException
