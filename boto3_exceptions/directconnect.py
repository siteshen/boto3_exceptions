import boto3

exceptions = boto3.client('directconnect').exceptions

DirectConnectClientException = exceptions.DirectConnectClientException
DirectConnectServerException = exceptions.DirectConnectServerException
DuplicateTagKeysException = exceptions.DuplicateTagKeysException
TooManyTagsException = exceptions.TooManyTagsException
