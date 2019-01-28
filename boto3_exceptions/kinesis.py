import boto3

exceptions = boto3.client('kinesis').exceptions

ExpiredIteratorException = exceptions.ExpiredIteratorException
ExpiredNextTokenException = exceptions.ExpiredNextTokenException
InternalFailureException = exceptions.InternalFailureException
InvalidArgumentException = exceptions.InvalidArgumentException
KMSAccessDeniedException = exceptions.KMSAccessDeniedException
KMSDisabledException = exceptions.KMSDisabledException
KMSInvalidStateException = exceptions.KMSInvalidStateException
KMSNotFoundException = exceptions.KMSNotFoundException
KMSOptInRequired = exceptions.KMSOptInRequired
KMSThrottlingException = exceptions.KMSThrottlingException
LimitExceededException = exceptions.LimitExceededException
ProvisionedThroughputExceededException = exceptions.ProvisionedThroughputExceededException
ResourceInUseException = exceptions.ResourceInUseException
ResourceNotFoundException = exceptions.ResourceNotFoundException
