import boto3

exceptions = boto3.client('cloudwatch').exceptions

InvalidParameterInput = exceptions.InvalidParameterInput
ResourceNotFound = exceptions.ResourceNotFound
InternalServiceError = exceptions.InternalServiceError
InvalidFormat = exceptions.InvalidFormat
InvalidNextToken = exceptions.InvalidNextToken
InvalidParameterCombination = exceptions.InvalidParameterCombination
InvalidParameterValue = exceptions.InvalidParameterValue
LimitExceeded = exceptions.LimitExceeded
MissingParameter = exceptions.MissingParameter
