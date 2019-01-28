import boto3

exceptions = boto3.client('storagegateway').exceptions

InternalServerError = exceptions.InternalServerError
InvalidGatewayRequestException = exceptions.InvalidGatewayRequestException
ServiceUnavailableError = exceptions.ServiceUnavailableError
