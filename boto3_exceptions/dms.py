import boto3

exceptions = boto3.client('dms').exceptions

AccessDeniedFault = exceptions.AccessDeniedFault
InsufficientResourceCapacityFault = exceptions.InsufficientResourceCapacityFault
InvalidCertificateFault = exceptions.InvalidCertificateFault
InvalidResourceStateFault = exceptions.InvalidResourceStateFault
InvalidSubnet = exceptions.InvalidSubnet
KMSKeyNotAccessibleFault = exceptions.KMSKeyNotAccessibleFault
ReplicationSubnetGroupDoesNotCoverEnoughAZs = exceptions.ReplicationSubnetGroupDoesNotCoverEnoughAZs
ResourceAlreadyExistsFault = exceptions.ResourceAlreadyExistsFault
ResourceNotFoundFault = exceptions.ResourceNotFoundFault
ResourceQuotaExceededFault = exceptions.ResourceQuotaExceededFault
SNSInvalidTopicFault = exceptions.SNSInvalidTopicFault
SNSNoAuthorizationFault = exceptions.SNSNoAuthorizationFault
StorageQuotaExceededFault = exceptions.StorageQuotaExceededFault
SubnetAlreadyInUse = exceptions.SubnetAlreadyInUse
UpgradeDependencyFailureFault = exceptions.UpgradeDependencyFailureFault