import boto3

exceptions = boto3.client('datasync').exceptions

InternalException = exceptions.InternalException
InvalidRequestException = exceptions.InvalidRequestException
