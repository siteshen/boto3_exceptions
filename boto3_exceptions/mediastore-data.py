import boto3

exceptions = boto3.client('mediastore-data').exceptions

ContainerNotFoundException = exceptions.ContainerNotFoundException
InternalServerError = exceptions.InternalServerError
ObjectNotFoundException = exceptions.ObjectNotFoundException
RequestedRangeNotSatisfiableException = exceptions.RequestedRangeNotSatisfiableException
