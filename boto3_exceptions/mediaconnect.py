import boto3

exceptions = boto3.client('mediaconnect').exceptions

AddFlowOutputs420Exception = exceptions.AddFlowOutputs420Exception
BadRequestException = exceptions.BadRequestException
CreateFlow420Exception = exceptions.CreateFlow420Exception
ForbiddenException = exceptions.ForbiddenException
GrantFlowEntitlements420Exception = exceptions.GrantFlowEntitlements420Exception
InternalServerErrorException = exceptions.InternalServerErrorException
NotFoundException = exceptions.NotFoundException
ServiceUnavailableException = exceptions.ServiceUnavailableException
TooManyRequestsException = exceptions.TooManyRequestsException