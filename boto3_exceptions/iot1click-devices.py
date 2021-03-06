import boto3

exceptions = boto3.client('iot1click-devices').exceptions

ForbiddenException = exceptions.ForbiddenException
InternalFailureException = exceptions.InternalFailureException
InvalidRequestException = exceptions.InvalidRequestException
PreconditionFailedException = exceptions.PreconditionFailedException
RangeNotSatisfiableException = exceptions.RangeNotSatisfiableException
ResourceConflictException = exceptions.ResourceConflictException
ResourceNotFoundException = exceptions.ResourceNotFoundException
