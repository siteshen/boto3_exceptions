import boto3

exceptions = boto3.client('personalize-runtime').exceptions

InvalidInputException = exceptions.InvalidInputException
ResourceNotFoundException = exceptions.ResourceNotFoundException
