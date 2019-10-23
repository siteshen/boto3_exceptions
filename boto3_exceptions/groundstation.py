import boto3

exceptions = boto3.client('groundstation').exceptions

InvalidParameterException = exceptions.InvalidParameterException
DependencyException = exceptions.DependencyException
ResourceNotFoundException = exceptions.ResourceNotFoundException
