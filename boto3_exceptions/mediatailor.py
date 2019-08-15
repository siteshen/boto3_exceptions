import boto3

exceptions = boto3.client('mediatailor').exceptions

BadRequestException = exceptions.BadRequestException
