import boto3

exceptions = boto3.client('apigatewaymanagementapi').exceptions

ForbiddenException = exceptions.ForbiddenException
GoneException = exceptions.GoneException
LimitExceededException = exceptions.LimitExceededException
PayloadTooLargeException = exceptions.PayloadTooLargeException
