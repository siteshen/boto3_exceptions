import boto3

exceptions = boto3.client('workmailmessageflow').exceptions

ResourceNotFoundException = exceptions.ResourceNotFoundException
