import boto3

exceptions = boto3.client('cloudformation').exceptions

AlreadyExistsException = exceptions.AlreadyExistsException
ChangeSetNotFound = exceptions.ChangeSetNotFound
CreatedButModifiedException = exceptions.CreatedButModifiedException
InsufficientCapabilitiesException = exceptions.InsufficientCapabilitiesException
InvalidChangeSetStatus = exceptions.InvalidChangeSetStatus
InvalidOperationException = exceptions.InvalidOperationException
LimitExceededException = exceptions.LimitExceededException
NameAlreadyExistsException = exceptions.NameAlreadyExistsException
OperationIdAlreadyExistsException = exceptions.OperationIdAlreadyExistsException
OperationInProgressException = exceptions.OperationInProgressException
OperationNotFoundException = exceptions.OperationNotFoundException
StackInstanceNotFoundException = exceptions.StackInstanceNotFoundException
StackSetNotEmptyException = exceptions.StackSetNotEmptyException
StackSetNotFoundException = exceptions.StackSetNotFoundException
StaleRequestException = exceptions.StaleRequestException
TokenAlreadyExistsException = exceptions.TokenAlreadyExistsException