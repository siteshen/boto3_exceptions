import boto3

exceptions = boto3.client('greengrass').exceptions

BadRequestException = exceptions.BadRequestException
InternalServerErrorException = exceptions.InternalServerErrorException
