import boto3

exceptions = boto3.client('sagemaker-runtime').exceptions

InternalFailure = exceptions.InternalFailure
ModelError = exceptions.ModelError
ServiceUnavailable = exceptions.ServiceUnavailable
ValidationError = exceptions.ValidationError
