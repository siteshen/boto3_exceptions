import boto3

exceptions = boto3.client('globalaccelerator').exceptions

AcceleratorNotDisabledException = exceptions.AcceleratorNotDisabledException
AcceleratorNotFoundException = exceptions.AcceleratorNotFoundException
AccessDeniedException = exceptions.AccessDeniedException
AssociatedEndpointGroupFoundException = exceptions.AssociatedEndpointGroupFoundException
AssociatedListenerFoundException = exceptions.AssociatedListenerFoundException
EndpointGroupAlreadyExistsException = exceptions.EndpointGroupAlreadyExistsException
EndpointGroupNotFoundException = exceptions.EndpointGroupNotFoundException
InternalServiceErrorException = exceptions.InternalServiceErrorException
InvalidArgumentException = exceptions.InvalidArgumentException
InvalidNextTokenException = exceptions.InvalidNextTokenException
InvalidPortRangeException = exceptions.InvalidPortRangeException
LimitExceededException = exceptions.LimitExceededException
ListenerNotFoundException = exceptions.ListenerNotFoundException
