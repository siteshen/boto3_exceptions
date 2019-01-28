import boto3

exceptions = boto3.client('mgh').exceptions

AccessDeniedException = exceptions.AccessDeniedException
DryRunOperation = exceptions.DryRunOperation
InternalServerError = exceptions.InternalServerError
InvalidInputException = exceptions.InvalidInputException
PolicyErrorException = exceptions.PolicyErrorException
ResourceNotFoundException = exceptions.ResourceNotFoundException
ServiceUnavailableException = exceptions.ServiceUnavailableException
UnauthorizedOperation = exceptions.UnauthorizedOperation
