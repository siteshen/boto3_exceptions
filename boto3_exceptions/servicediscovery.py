import boto3

exceptions = boto3.client('servicediscovery').exceptions

CustomHealthNotFound = exceptions.CustomHealthNotFound
DuplicateRequest = exceptions.DuplicateRequest
InstanceNotFound = exceptions.InstanceNotFound
InvalidInput = exceptions.InvalidInput
NamespaceAlreadyExists = exceptions.NamespaceAlreadyExists
NamespaceNotFound = exceptions.NamespaceNotFound
OperationNotFound = exceptions.OperationNotFound
ResourceInUse = exceptions.ResourceInUse
ResourceLimitExceeded = exceptions.ResourceLimitExceeded
ServiceAlreadyExists = exceptions.ServiceAlreadyExists
ServiceNotFound = exceptions.ServiceNotFound
