import boto3

exceptions = boto3.client('acm').exceptions

InvalidArgsException = exceptions.InvalidArgsException
InvalidArnException = exceptions.InvalidArnException
InvalidDomainValidationOptionsException = exceptions.InvalidDomainValidationOptionsException
InvalidStateException = exceptions.InvalidStateException
InvalidTagException = exceptions.InvalidTagException
LimitExceededException = exceptions.LimitExceededException
RequestInProgressException = exceptions.RequestInProgressException
ResourceInUseException = exceptions.ResourceInUseException
ResourceNotFoundException = exceptions.ResourceNotFoundException
TooManyTagsException = exceptions.TooManyTagsException
