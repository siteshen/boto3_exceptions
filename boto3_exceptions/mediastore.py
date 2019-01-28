import boto3

exceptions = boto3.client('mediastore').exceptions

ContainerInUseException = exceptions.ContainerInUseException
ContainerNotFoundException = exceptions.ContainerNotFoundException
CorsPolicyNotFoundException = exceptions.CorsPolicyNotFoundException
InternalServerError = exceptions.InternalServerError
LimitExceededException = exceptions.LimitExceededException
PolicyNotFoundException = exceptions.PolicyNotFoundException
