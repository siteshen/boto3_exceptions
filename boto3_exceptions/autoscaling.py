import boto3

exceptions = boto3.client('autoscaling').exceptions

AlreadyExists = exceptions.AlreadyExists
InvalidNextToken = exceptions.InvalidNextToken
LimitExceeded = exceptions.LimitExceeded
ResourceContention = exceptions.ResourceContention
ResourceInUse = exceptions.ResourceInUse
ScalingActivityInProgress = exceptions.ScalingActivityInProgress
ServiceLinkedRoleFailure = exceptions.ServiceLinkedRoleFailure
