import boto3

exceptions = boto3.client('cloudsearch').exceptions

BaseException = exceptions.BaseException
DisabledAction = exceptions.DisabledAction
InternalException = exceptions.InternalException
InvalidType = exceptions.InvalidType
LimitExceeded = exceptions.LimitExceeded
ResourceNotFound = exceptions.ResourceNotFound
