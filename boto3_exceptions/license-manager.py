import boto3

exceptions = boto3.client('license-manager').exceptions

AccessDeniedException = exceptions.AccessDeniedException
AuthorizationException = exceptions.AuthorizationException
FailedDependencyException = exceptions.FailedDependencyException
FilterLimitExceededException = exceptions.FilterLimitExceededException
InvalidParameterValueException = exceptions.InvalidParameterValueException
InvalidResourceStateException = exceptions.InvalidResourceStateException
LicenseUsageException = exceptions.LicenseUsageException
RateLimitExceededException = exceptions.RateLimitExceededException
ResourceLimitExceededException = exceptions.ResourceLimitExceededException
ServerInternalException = exceptions.ServerInternalException
