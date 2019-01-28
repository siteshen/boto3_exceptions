import boto3

exceptions = boto3.client('route53domains').exceptions

DomainLimitExceeded = exceptions.DomainLimitExceeded
DuplicateRequest = exceptions.DuplicateRequest
InvalidInput = exceptions.InvalidInput
OperationLimitExceeded = exceptions.OperationLimitExceeded
TLDRulesViolation = exceptions.TLDRulesViolation
UnsupportedTLD = exceptions.UnsupportedTLD
