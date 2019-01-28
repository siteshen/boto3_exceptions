import boto3

exceptions = boto3.client('mturk').exceptions

RequestError = exceptions.RequestError
ServiceFault = exceptions.ServiceFault
