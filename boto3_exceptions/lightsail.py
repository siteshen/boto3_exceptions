import boto3

exceptions = boto3.client('lightsail').exceptions

AccessDeniedException = exceptions.AccessDeniedException
AccountSetupInProgressException = exceptions.AccountSetupInProgressException
InvalidInputException = exceptions.InvalidInputException
NotFoundException = exceptions.NotFoundException
OperationFailureException = exceptions.OperationFailureException
ServiceException = exceptions.ServiceException
UnauthenticatedException = exceptions.UnauthenticatedException
