import boto3

exceptions = boto3.client('cloudtrail').exceptions

CloudTrailARNInvalidException = exceptions.CloudTrailARNInvalidException
CloudTrailAccessNotEnabledException = exceptions.CloudTrailAccessNotEnabledException
CloudWatchLogsDeliveryUnavailableException = exceptions.CloudWatchLogsDeliveryUnavailableException
InsufficientDependencyServiceAccessPermissionException = exceptions.InsufficientDependencyServiceAccessPermissionException
InsufficientEncryptionPolicyException = exceptions.InsufficientEncryptionPolicyException
InsufficientS3BucketPolicyException = exceptions.InsufficientS3BucketPolicyException
InsufficientSnsTopicPolicyException = exceptions.InsufficientSnsTopicPolicyException
InvalidCloudWatchLogsLogGroupArnException = exceptions.InvalidCloudWatchLogsLogGroupArnException
InvalidCloudWatchLogsRoleArnException = exceptions.InvalidCloudWatchLogsRoleArnException
InvalidEventSelectorsException = exceptions.InvalidEventSelectorsException
InvalidHomeRegionException = exceptions.InvalidHomeRegionException
InvalidKmsKeyIdException = exceptions.InvalidKmsKeyIdException
InvalidLookupAttributesException = exceptions.InvalidLookupAttributesException
InvalidMaxResultsException = exceptions.InvalidMaxResultsException
InvalidNextTokenException = exceptions.InvalidNextTokenException
InvalidParameterCombinationException = exceptions.InvalidParameterCombinationException
InvalidS3BucketNameException = exceptions.InvalidS3BucketNameException
InvalidS3PrefixException = exceptions.InvalidS3PrefixException
InvalidSnsTopicNameException = exceptions.InvalidSnsTopicNameException
InvalidTagParameterException = exceptions.InvalidTagParameterException
InvalidTimeRangeException = exceptions.InvalidTimeRangeException
InvalidTokenException = exceptions.InvalidTokenException
InvalidTrailNameException = exceptions.InvalidTrailNameException
KmsException = exceptions.KmsException
KmsKeyDisabledException = exceptions.KmsKeyDisabledException
KmsKeyNotFoundException = exceptions.KmsKeyNotFoundException
MaximumNumberOfTrailsExceededException = exceptions.MaximumNumberOfTrailsExceededException
NotOrganizationMasterAccountException = exceptions.NotOrganizationMasterAccountException
OperationNotPermittedException = exceptions.OperationNotPermittedException
OrganizationNotInAllFeaturesModeException = exceptions.OrganizationNotInAllFeaturesModeException
OrganizationsNotInUseException = exceptions.OrganizationsNotInUseException
ResourceNotFoundException = exceptions.ResourceNotFoundException
ResourceTypeNotSupportedException = exceptions.ResourceTypeNotSupportedException
S3BucketDoesNotExistException = exceptions.S3BucketDoesNotExistException
TagsLimitExceededException = exceptions.TagsLimitExceededException
TrailAlreadyExistsException = exceptions.TrailAlreadyExistsException
TrailNotFoundException = exceptions.TrailNotFoundException
TrailNotProvidedException = exceptions.TrailNotProvidedException
UnsupportedOperationException = exceptions.UnsupportedOperationException
