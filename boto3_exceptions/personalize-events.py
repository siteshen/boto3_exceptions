import boto3

exceptions = boto3.client('personalize-events').exceptions

InvalidInputException = exceptions.InvalidInputException
