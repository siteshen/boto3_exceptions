import boto3

exceptions = boto3.client('rds').exceptions

AuthorizationAlreadyExists = exceptions.AuthorizationAlreadyExists
AuthorizationNotFound = exceptions.AuthorizationNotFound
AuthorizationQuotaExceeded = exceptions.AuthorizationQuotaExceeded
BackupPolicyNotFoundFault = exceptions.BackupPolicyNotFoundFault
CertificateNotFound = exceptions.CertificateNotFound
DBClusterAlreadyExistsFault = exceptions.DBClusterAlreadyExistsFault
DBClusterBacktrackNotFoundFault = exceptions.DBClusterBacktrackNotFoundFault
DBClusterEndpointAlreadyExistsFault = exceptions.DBClusterEndpointAlreadyExistsFault
DBClusterEndpointNotFoundFault = exceptions.DBClusterEndpointNotFoundFault
DBClusterEndpointQuotaExceededFault = exceptions.DBClusterEndpointQuotaExceededFault
DBClusterNotFoundFault = exceptions.DBClusterNotFoundFault
DBClusterParameterGroupNotFound = exceptions.DBClusterParameterGroupNotFound
DBClusterQuotaExceededFault = exceptions.DBClusterQuotaExceededFault
DBClusterRoleAlreadyExists = exceptions.DBClusterRoleAlreadyExists
DBClusterRoleNotFound = exceptions.DBClusterRoleNotFound
DBClusterRoleQuotaExceeded = exceptions.DBClusterRoleQuotaExceeded
DBClusterSnapshotAlreadyExistsFault = exceptions.DBClusterSnapshotAlreadyExistsFault
DBClusterSnapshotNotFoundFault = exceptions.DBClusterSnapshotNotFoundFault
DBInstanceAlreadyExists = exceptions.DBInstanceAlreadyExists
DBInstanceAutomatedBackupNotFound = exceptions.DBInstanceAutomatedBackupNotFound
DBInstanceAutomatedBackupQuotaExceeded = exceptions.DBInstanceAutomatedBackupQuotaExceeded
DBInstanceNotFound = exceptions.DBInstanceNotFound
DBInstanceRoleAlreadyExists = exceptions.DBInstanceRoleAlreadyExists
DBInstanceRoleNotFound = exceptions.DBInstanceRoleNotFound
DBInstanceRoleQuotaExceeded = exceptions.DBInstanceRoleQuotaExceeded
DBLogFileNotFoundFault = exceptions.DBLogFileNotFoundFault
DBParameterGroupAlreadyExists = exceptions.DBParameterGroupAlreadyExists
DBParameterGroupNotFound = exceptions.DBParameterGroupNotFound
DBParameterGroupQuotaExceeded = exceptions.DBParameterGroupQuotaExceeded
DBSecurityGroupAlreadyExists = exceptions.DBSecurityGroupAlreadyExists
DBSecurityGroupNotFound = exceptions.DBSecurityGroupNotFound
DBSecurityGroupNotSupported = exceptions.DBSecurityGroupNotSupported
QuotaExceeded.DBSecurityGroup = exceptions.QuotaExceeded.DBSecurityGroup
DBSnapshotAlreadyExists = exceptions.DBSnapshotAlreadyExists
DBSnapshotNotFound = exceptions.DBSnapshotNotFound
DBSubnetGroupAlreadyExists = exceptions.DBSubnetGroupAlreadyExists
DBSubnetGroupDoesNotCoverEnoughAZs = exceptions.DBSubnetGroupDoesNotCoverEnoughAZs
DBSubnetGroupNotAllowedFault = exceptions.DBSubnetGroupNotAllowedFault
DBSubnetGroupNotFoundFault = exceptions.DBSubnetGroupNotFoundFault
DBSubnetGroupQuotaExceeded = exceptions.DBSubnetGroupQuotaExceeded
DBSubnetQuotaExceededFault = exceptions.DBSubnetQuotaExceededFault
DBUpgradeDependencyFailure = exceptions.DBUpgradeDependencyFailure
DomainNotFoundFault = exceptions.DomainNotFoundFault
EventSubscriptionQuotaExceeded = exceptions.EventSubscriptionQuotaExceeded
GlobalClusterAlreadyExistsFault = exceptions.GlobalClusterAlreadyExistsFault
GlobalClusterNotFoundFault = exceptions.GlobalClusterNotFoundFault
GlobalClusterQuotaExceededFault = exceptions.GlobalClusterQuotaExceededFault
InstanceQuotaExceeded = exceptions.InstanceQuotaExceeded
InsufficientDBClusterCapacityFault = exceptions.InsufficientDBClusterCapacityFault
InsufficientDBInstanceCapacity = exceptions.InsufficientDBInstanceCapacity
InsufficientStorageClusterCapacity = exceptions.InsufficientStorageClusterCapacity
InvalidDBClusterCapacityFault = exceptions.InvalidDBClusterCapacityFault
InvalidDBClusterEndpointStateFault = exceptions.InvalidDBClusterEndpointStateFault
InvalidDBClusterSnapshotStateFault = exceptions.InvalidDBClusterSnapshotStateFault
InvalidDBClusterStateFault = exceptions.InvalidDBClusterStateFault
InvalidDBInstanceAutomatedBackupState = exceptions.InvalidDBInstanceAutomatedBackupState
InvalidDBInstanceState = exceptions.InvalidDBInstanceState
InvalidDBParameterGroupState = exceptions.InvalidDBParameterGroupState
InvalidDBSecurityGroupState = exceptions.InvalidDBSecurityGroupState
InvalidDBSnapshotState = exceptions.InvalidDBSnapshotState
InvalidDBSubnetGroupFault = exceptions.InvalidDBSubnetGroupFault
InvalidDBSubnetGroupStateFault = exceptions.InvalidDBSubnetGroupStateFault
InvalidDBSubnetStateFault = exceptions.InvalidDBSubnetStateFault
InvalidEventSubscriptionState = exceptions.InvalidEventSubscriptionState
InvalidGlobalClusterStateFault = exceptions.InvalidGlobalClusterStateFault
InvalidOptionGroupStateFault = exceptions.InvalidOptionGroupStateFault
InvalidRestoreFault = exceptions.InvalidRestoreFault
InvalidS3BucketFault = exceptions.InvalidS3BucketFault
InvalidSubnet = exceptions.InvalidSubnet
InvalidVPCNetworkStateFault = exceptions.InvalidVPCNetworkStateFault
KMSKeyNotAccessibleFault = exceptions.KMSKeyNotAccessibleFault
OptionGroupAlreadyExistsFault = exceptions.OptionGroupAlreadyExistsFault
OptionGroupNotFoundFault = exceptions.OptionGroupNotFoundFault
OptionGroupQuotaExceededFault = exceptions.OptionGroupQuotaExceededFault
PointInTimeRestoreNotEnabled = exceptions.PointInTimeRestoreNotEnabled
ProvisionedIopsNotAvailableInAZFault = exceptions.ProvisionedIopsNotAvailableInAZFault
ReservedDBInstanceAlreadyExists = exceptions.ReservedDBInstanceAlreadyExists
ReservedDBInstanceNotFound = exceptions.ReservedDBInstanceNotFound
ReservedDBInstanceQuotaExceeded = exceptions.ReservedDBInstanceQuotaExceeded
ReservedDBInstancesOfferingNotFound = exceptions.ReservedDBInstancesOfferingNotFound
ResourceNotFoundFault = exceptions.ResourceNotFoundFault
SNSInvalidTopic = exceptions.SNSInvalidTopic
SNSNoAuthorization = exceptions.SNSNoAuthorization
SNSTopicArnNotFound = exceptions.SNSTopicArnNotFound
SharedSnapshotQuotaExceeded = exceptions.SharedSnapshotQuotaExceeded
SnapshotQuotaExceeded = exceptions.SnapshotQuotaExceeded
SourceNotFound = exceptions.SourceNotFound
StorageQuotaExceeded = exceptions.StorageQuotaExceeded
StorageTypeNotSupported = exceptions.StorageTypeNotSupported
SubnetAlreadyInUse = exceptions.SubnetAlreadyInUse
SubscriptionAlreadyExist = exceptions.SubscriptionAlreadyExist
SubscriptionCategoryNotFound = exceptions.SubscriptionCategoryNotFound
SubscriptionNotFound = exceptions.SubscriptionNotFound