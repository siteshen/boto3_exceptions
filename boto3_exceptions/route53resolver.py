import boto3

exceptions = boto3.client('route53resolver').exceptions

InternalServiceErrorException = exceptions.InternalServiceErrorException
InvalidNextTokenException = exceptions.InvalidNextTokenException
InvalidParameterException = exceptions.InvalidParameterException
InvalidPolicyDocument = exceptions.InvalidPolicyDocument
InvalidRequestException = exceptions.InvalidRequestException
InvalidTagException = exceptions.InvalidTagException
LimitExceededException = exceptions.LimitExceededException
ResourceExistsException = exceptions.ResourceExistsException
ResourceInUseException = exceptions.ResourceInUseException
ResourceNotFoundException = exceptions.ResourceNotFoundException
ResourceUnavailableException = exceptions.ResourceUnavailableException
ThrottlingException = exceptions.ThrottlingException
UnknownResourceException = exceptions.UnknownResourceException
