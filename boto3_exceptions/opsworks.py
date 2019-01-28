import boto3

exceptions = boto3.client('opsworks').exceptions

ResourceNotFoundException = exceptions.ResourceNotFoundException
ValidationException = exceptions.ValidationException
