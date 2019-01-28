import boto3

exceptions = boto3.client('macie').exceptions

AccessDeniedException = exceptions.AccessDeniedException
InternalException = exceptions.InternalException
InvalidInputException = exceptions.InvalidInputException
LimitExceededException = exceptions.LimitExceededException
