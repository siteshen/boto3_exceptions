import boto3

exceptions = boto3.client('emr').exceptions

InternalServerError = exceptions.InternalServerError
InternalServerException = exceptions.InternalServerException
InvalidRequestException = exceptions.InvalidRequestException
