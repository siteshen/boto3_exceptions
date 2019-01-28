import boto3

exceptions = boto3.client('batch').exceptions

ClientException = exceptions.ClientException
ServerException = exceptions.ServerException
