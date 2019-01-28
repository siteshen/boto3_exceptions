import boto3

exceptions = boto3.client('health').exceptions

InvalidPaginationToken = exceptions.InvalidPaginationToken
UnsupportedLocale = exceptions.UnsupportedLocale
