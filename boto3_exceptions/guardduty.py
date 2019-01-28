import boto3

exceptions = boto3.client('guardduty').exceptions

BadRequestException = exceptions.BadRequestException
InternalServerErrorException = exceptions.InternalServerErrorException
