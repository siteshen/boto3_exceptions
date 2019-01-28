import boto3

exceptions = boto3.client('cloudsearchdomain').exceptions

DocumentServiceException = exceptions.DocumentServiceException
SearchException = exceptions.SearchException
