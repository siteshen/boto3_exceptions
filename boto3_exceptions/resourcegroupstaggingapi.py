import boto3

exceptions = boto3.client('resourcegroupstaggingapi').exceptions

InternalServiceException = exceptions.InternalServiceException
InvalidParameterException = exceptions.InvalidParameterException
PaginationTokenExpiredException = exceptions.PaginationTokenExpiredException
ThrottledException = exceptions.ThrottledException
