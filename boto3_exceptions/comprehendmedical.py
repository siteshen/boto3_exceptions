import boto3

exceptions = boto3.client('comprehendmedical').exceptions

InternalServerException = exceptions.InternalServerException
InvalidEncodingException = exceptions.InvalidEncodingException
InvalidRequestException = exceptions.InvalidRequestException
ServiceUnavailableException = exceptions.ServiceUnavailableException
TextSizeLimitExceededException = exceptions.TextSizeLimitExceededException
TooManyRequestsException = exceptions.TooManyRequestsException
