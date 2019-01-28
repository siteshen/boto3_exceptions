import boto3

exceptions = boto3.client('xray').exceptions

InvalidRequestException = exceptions.InvalidRequestException
RuleLimitExceededException = exceptions.RuleLimitExceededException
ThrottledException = exceptions.ThrottledException
