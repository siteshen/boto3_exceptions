import boto3

exceptions = boto3.client('s3control').exceptions

NoSuchPublicAccessBlockConfiguration = exceptions.NoSuchPublicAccessBlockConfiguration
