import boto3

exceptions = boto3.client('sagemaker').exceptions

ResourceInUse = exceptions.ResourceInUse
ResourceLimitExceeded = exceptions.ResourceLimitExceeded
ResourceNotFound = exceptions.ResourceNotFound
