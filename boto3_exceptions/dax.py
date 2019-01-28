import boto3

exceptions = boto3.client('dax').exceptions

ClusterAlreadyExistsFault = exceptions.ClusterAlreadyExistsFault
ClusterNotFoundFault = exceptions.ClusterNotFoundFault
ClusterQuotaForCustomerExceededFault = exceptions.ClusterQuotaForCustomerExceededFault
InsufficientClusterCapacityFault = exceptions.InsufficientClusterCapacityFault
InvalidARNFault = exceptions.InvalidARNFault
InvalidClusterStateFault = exceptions.InvalidClusterStateFault
InvalidParameterCombinationException = exceptions.InvalidParameterCombinationException
InvalidParameterGroupStateFault = exceptions.InvalidParameterGroupStateFault
InvalidParameterValueException = exceptions.InvalidParameterValueException
InvalidSubnet = exceptions.InvalidSubnet
InvalidVPCNetworkStateFault = exceptions.InvalidVPCNetworkStateFault
NodeNotFoundFault = exceptions.NodeNotFoundFault
NodeQuotaForClusterExceededFault = exceptions.NodeQuotaForClusterExceededFault
NodeQuotaForCustomerExceededFault = exceptions.NodeQuotaForCustomerExceededFault
ParameterGroupAlreadyExistsFault = exceptions.ParameterGroupAlreadyExistsFault
ParameterGroupNotFoundFault = exceptions.ParameterGroupNotFoundFault
ParameterGroupQuotaExceededFault = exceptions.ParameterGroupQuotaExceededFault
ServiceLinkedRoleNotFoundFault = exceptions.ServiceLinkedRoleNotFoundFault
SubnetGroupAlreadyExistsFault = exceptions.SubnetGroupAlreadyExistsFault
SubnetGroupInUseFault = exceptions.SubnetGroupInUseFault
SubnetGroupNotFoundFault = exceptions.SubnetGroupNotFoundFault
SubnetGroupQuotaExceededFault = exceptions.SubnetGroupQuotaExceededFault
SubnetInUse = exceptions.SubnetInUse
SubnetQuotaExceededFault = exceptions.SubnetQuotaExceededFault
TagNotFoundFault = exceptions.TagNotFoundFault
TagQuotaPerResourceExceeded = exceptions.TagQuotaPerResourceExceeded
