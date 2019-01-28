import boto3

exceptions = boto3.client('iam').exceptions

ConcurrentModification = exceptions.ConcurrentModification
ReportExpired = exceptions.ReportExpired
ReportNotPresent = exceptions.ReportNotPresent
ReportInProgress = exceptions.ReportInProgress
DeleteConflict = exceptions.DeleteConflict
DuplicateCertificate = exceptions.DuplicateCertificate
DuplicateSSHPublicKey = exceptions.DuplicateSSHPublicKey
EntityAlreadyExists = exceptions.EntityAlreadyExists
EntityTemporarilyUnmodifiable = exceptions.EntityTemporarilyUnmodifiable
InvalidAuthenticationCode = exceptions.InvalidAuthenticationCode
InvalidCertificate = exceptions.InvalidCertificate
InvalidInput = exceptions.InvalidInput
InvalidPublicKey = exceptions.InvalidPublicKey
InvalidUserType = exceptions.InvalidUserType
KeyPairMismatch = exceptions.KeyPairMismatch
LimitExceeded = exceptions.LimitExceeded
MalformedCertificate = exceptions.MalformedCertificate
MalformedPolicyDocument = exceptions.MalformedPolicyDocument
NoSuchEntity = exceptions.NoSuchEntity
PasswordPolicyViolation = exceptions.PasswordPolicyViolation
PolicyEvaluation = exceptions.PolicyEvaluation
PolicyNotAttachable = exceptions.PolicyNotAttachable
ServiceFailure = exceptions.ServiceFailure
NotSupportedService = exceptions.NotSupportedService
UnmodifiableEntity = exceptions.UnmodifiableEntity
UnrecognizedPublicKeyEncoding = exceptions.UnrecognizedPublicKeyEncoding
