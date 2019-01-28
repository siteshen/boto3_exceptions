import boto3

exceptions = boto3.client('ce').exceptions

BillExpirationException = exceptions.BillExpirationException
DataUnavailableException = exceptions.DataUnavailableException
InvalidNextTokenException = exceptions.InvalidNextTokenException
LimitExceededException = exceptions.LimitExceededException
RequestChangedException = exceptions.RequestChangedException
