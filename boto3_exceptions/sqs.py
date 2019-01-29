import boto3

exceptions = boto3.client('sqs').exceptions

BatchEntryIdsNotDistinct = exceptions.BatchEntryIdsNotDistinct
BatchRequestTooLong = exceptions.BatchRequestTooLong
EmptyBatchRequest = exceptions.EmptyBatchRequest
InvalidAttributeName = exceptions.InvalidAttributeName
InvalidBatchEntryId = exceptions.InvalidBatchEntryId
InvalidIdFormat = exceptions.InvalidIdFormat
InvalidMessageContents = exceptions.InvalidMessageContents
MessageNotInflight = exceptions.MessageNotInflight
OverLimit = exceptions.OverLimit
PurgeQueueInProgress = exceptions.PurgeQueueInProgress
QueueDeletedRecently = exceptions.QueueDeletedRecently
QueueDoesNotExist = exceptions.QueueDoesNotExist
QueueNameExists = exceptions.QueueNameExists
ReceiptHandleIsInvalid = exceptions.ReceiptHandleIsInvalid
TooManyEntriesInBatchRequest = exceptions.TooManyEntriesInBatchRequest
UnsupportedOperation = exceptions.UnsupportedOperation
