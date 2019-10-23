import boto3

exceptions = boto3.client('apigatewaymanagementapi').exceptions

ForbiddenException = exceptions.ForbiddenException
GoneException = exceptions.GoneException
PayloadTooLargeException = exceptions.PayloadTooLargeException
LimitExceededException = exceptions.LimitExceededException
