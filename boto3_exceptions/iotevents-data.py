import boto3

exceptions = boto3.client('iotevents-data').exceptions

InternalFailureException = exceptions.InternalFailureException
InvalidRequestException = exceptions.InvalidRequestException
ResourceNotFoundException = exceptions.ResourceNotFoundException
ServiceUnavailableException = exceptions.ServiceUnavailableException
ThrottlingException = exceptions.ThrottlingException
