import boto3

exceptions = boto3.client('apigatewayv2').exceptions

BadRequestException = exceptions.BadRequestException
ConflictException = exceptions.ConflictException
NotFoundException = exceptions.NotFoundException
TooManyRequestsException = exceptions.TooManyRequestsException
