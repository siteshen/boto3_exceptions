import boto3

exceptions = boto3.client('snowball').exceptions

ClusterLimitExceededException = exceptions.ClusterLimitExceededException
Ec2RequestFailedException = exceptions.Ec2RequestFailedException
InvalidAddressException = exceptions.InvalidAddressException
InvalidInputCombinationException = exceptions.InvalidInputCombinationException
InvalidJobStateException = exceptions.InvalidJobStateException
InvalidNextTokenException = exceptions.InvalidNextTokenException
InvalidResourceException = exceptions.InvalidResourceException
KMSRequestFailedException = exceptions.KMSRequestFailedException
UnsupportedAddressException = exceptions.UnsupportedAddressException
