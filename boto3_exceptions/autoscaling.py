import boto3

exceptions = boto3.client('autoscaling').exceptions

AlreadyExistsFault = exceptions.AlreadyExistsFault
InvalidNextToken = exceptions.InvalidNextToken
LimitExceededFault = exceptions.LimitExceededFault
ResourceContentionFault = exceptions.ResourceContentionFault
ResourceInUseFault = exceptions.ResourceInUseFault
ScalingActivityInProgressFault = exceptions.ScalingActivityInProgressFault
ServiceLinkedRoleFailure = exceptions.ServiceLinkedRoleFailure
