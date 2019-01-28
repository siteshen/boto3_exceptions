import boto3

exceptions = boto3.client('sns').exceptions

AuthorizationError = exceptions.AuthorizationError
EndpointDisabled = exceptions.EndpointDisabled
FilterPolicyLimitExceeded = exceptions.FilterPolicyLimitExceeded
InternalError = exceptions.InternalError
InvalidParameter = exceptions.InvalidParameter
ParameterValueInvalid = exceptions.ParameterValueInvalid
InvalidSecurity = exceptions.InvalidSecurity
KMSAccessDenied = exceptions.KMSAccessDenied
KMSDisabled = exceptions.KMSDisabled
KMSInvalidState = exceptions.KMSInvalidState
KMSNotFound = exceptions.KMSNotFound
KMSOptInRequired = exceptions.KMSOptInRequired
KMSThrottling = exceptions.KMSThrottling
NotFound = exceptions.NotFound
PlatformApplicationDisabled = exceptions.PlatformApplicationDisabled
SubscriptionLimitExceeded = exceptions.SubscriptionLimitExceeded
Throttled = exceptions.Throttled
TopicLimitExceeded = exceptions.TopicLimitExceeded
