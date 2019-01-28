import boto3

exceptions = boto3.client('datapipeline').exceptions

InternalServiceError = exceptions.InternalServiceError
InvalidRequestException = exceptions.InvalidRequestException
PipelineDeletedException = exceptions.PipelineDeletedException
PipelineNotFoundException = exceptions.PipelineNotFoundException
TaskNotFoundException = exceptions.TaskNotFoundException
