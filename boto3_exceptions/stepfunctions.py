import boto3

exceptions = boto3.client('stepfunctions').exceptions

ActivityDoesNotExist = exceptions.ActivityDoesNotExist
ActivityLimitExceeded = exceptions.ActivityLimitExceeded
ActivityWorkerLimitExceeded = exceptions.ActivityWorkerLimitExceeded
ExecutionAlreadyExists = exceptions.ExecutionAlreadyExists
ExecutionDoesNotExist = exceptions.ExecutionDoesNotExist
ExecutionLimitExceeded = exceptions.ExecutionLimitExceeded
InvalidArn = exceptions.InvalidArn
InvalidDefinition = exceptions.InvalidDefinition
InvalidExecutionInput = exceptions.InvalidExecutionInput
InvalidName = exceptions.InvalidName
InvalidOutput = exceptions.InvalidOutput
InvalidToken = exceptions.InvalidToken
MissingRequiredParameter = exceptions.MissingRequiredParameter
ResourceNotFound = exceptions.ResourceNotFound
StateMachineAlreadyExists = exceptions.StateMachineAlreadyExists
StateMachineDeleting = exceptions.StateMachineDeleting
StateMachineDoesNotExist = exceptions.StateMachineDoesNotExist
StateMachineLimitExceeded = exceptions.StateMachineLimitExceeded
TaskDoesNotExist = exceptions.TaskDoesNotExist
TaskTimedOut = exceptions.TaskTimedOut
TooManyTags = exceptions.TooManyTags
