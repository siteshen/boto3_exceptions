import boto3

exceptions = boto3.client('datasync').exceptions

InvalidRequestException = exceptions.InvalidRequestException
