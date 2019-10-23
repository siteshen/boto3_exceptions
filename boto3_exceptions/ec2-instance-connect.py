import boto3

exceptions = boto3.client('ec2-instance-connect').exceptions

AuthException = exceptions.AuthException
EC2InstanceNotFoundException = exceptions.EC2InstanceNotFoundException
InvalidArgsException = exceptions.InvalidArgsException
ServiceException = exceptions.ServiceException
ThrottlingException = exceptions.ThrottlingException
