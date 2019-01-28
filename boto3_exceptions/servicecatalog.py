import boto3

exceptions = boto3.client('servicecatalog').exceptions

DuplicateResourceException = exceptions.DuplicateResourceException
InvalidParametersException = exceptions.InvalidParametersException
InvalidStateException = exceptions.InvalidStateException
LimitExceededException = exceptions.LimitExceededException
OperationNotSupportedException = exceptions.OperationNotSupportedException
ResourceInUseException = exceptions.ResourceInUseException
ResourceNotFoundException = exceptions.ResourceNotFoundException
TagOptionNotMigratedException = exceptions.TagOptionNotMigratedException
