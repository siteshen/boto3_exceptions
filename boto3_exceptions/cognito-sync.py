import boto3

exceptions = boto3.client('cognito-sync').exceptions

AlreadyStreamed = exceptions.AlreadyStreamed
ConcurrentModification = exceptions.ConcurrentModification
DuplicateRequest = exceptions.DuplicateRequest
InternalError = exceptions.InternalError
InvalidConfiguration = exceptions.InvalidConfiguration
InvalidLambdaFunctionOutput = exceptions.InvalidLambdaFunctionOutput
InvalidParameter = exceptions.InvalidParameter
LambdaThrottled = exceptions.LambdaThrottled
LimitExceeded = exceptions.LimitExceeded
NotAuthorizedError = exceptions.NotAuthorizedError
ResourceConflict = exceptions.ResourceConflict
ResourceNotFound = exceptions.ResourceNotFound
TooManyRequests = exceptions.TooManyRequests
