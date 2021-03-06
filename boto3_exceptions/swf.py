import boto3

exceptions = boto3.client('swf').exceptions

DefaultUndefinedFault = exceptions.DefaultUndefinedFault
DomainAlreadyExistsFault = exceptions.DomainAlreadyExistsFault
DomainDeprecatedFault = exceptions.DomainDeprecatedFault
LimitExceededFault = exceptions.LimitExceededFault
OperationNotPermittedFault = exceptions.OperationNotPermittedFault
TooManyTagsFault = exceptions.TooManyTagsFault
TypeAlreadyExistsFault = exceptions.TypeAlreadyExistsFault
TypeDeprecatedFault = exceptions.TypeDeprecatedFault
UnknownResourceFault = exceptions.UnknownResourceFault
WorkflowExecutionAlreadyStartedFault = exceptions.WorkflowExecutionAlreadyStartedFault
