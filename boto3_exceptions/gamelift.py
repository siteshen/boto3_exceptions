import boto3

exceptions = boto3.client('gamelift').exceptions

ConflictException = exceptions.ConflictException
FleetCapacityExceededException = exceptions.FleetCapacityExceededException
GameSessionFullException = exceptions.GameSessionFullException
IdempotentParameterMismatchException = exceptions.IdempotentParameterMismatchException
InternalServiceException = exceptions.InternalServiceException
InvalidFleetStatusException = exceptions.InvalidFleetStatusException
InvalidGameSessionStatusException = exceptions.InvalidGameSessionStatusException
InvalidRequestException = exceptions.InvalidRequestException
LimitExceededException = exceptions.LimitExceededException
NotFoundException = exceptions.NotFoundException
TerminalRoutingStrategyException = exceptions.TerminalRoutingStrategyException
UnauthorizedException = exceptions.UnauthorizedException
UnsupportedRegionException = exceptions.UnsupportedRegionException
