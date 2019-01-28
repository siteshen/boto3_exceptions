import boto3

exceptions = boto3.client('marketplace-entitlement').exceptions

InternalServiceErrorException = exceptions.InternalServiceErrorException
InvalidParameterException = exceptions.InvalidParameterException
ThrottlingException = exceptions.ThrottlingException
