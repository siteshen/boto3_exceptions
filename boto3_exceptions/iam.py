import boto3

exceptions = boto3.client('iam').exceptions

ConcurrentModificationException = exceptions.ConcurrentModificationException
CredentialReportExpiredException = exceptions.CredentialReportExpiredException
CredentialReportNotPresentException = exceptions.CredentialReportNotPresentException
CredentialReportNotReadyException = exceptions.CredentialReportNotReadyException
DeleteConflictException = exceptions.DeleteConflictException
DuplicateCertificateException = exceptions.DuplicateCertificateException
DuplicateSSHPublicKeyException = exceptions.DuplicateSSHPublicKeyException
EntityAlreadyExistsException = exceptions.EntityAlreadyExistsException
EntityTemporarilyUnmodifiableException = exceptions.EntityTemporarilyUnmodifiableException
InvalidAuthenticationCodeException = exceptions.InvalidAuthenticationCodeException
InvalidCertificateException = exceptions.InvalidCertificateException
InvalidInputException = exceptions.InvalidInputException
InvalidPublicKeyException = exceptions.InvalidPublicKeyException
InvalidUserTypeException = exceptions.InvalidUserTypeException
KeyPairMismatchException = exceptions.KeyPairMismatchException
LimitExceededException = exceptions.LimitExceededException
MalformedCertificateException = exceptions.MalformedCertificateException
MalformedPolicyDocumentException = exceptions.MalformedPolicyDocumentException
NoSuchEntityException = exceptions.NoSuchEntityException
PasswordPolicyViolationException = exceptions.PasswordPolicyViolationException
PolicyEvaluationException = exceptions.PolicyEvaluationException
PolicyNotAttachableException = exceptions.PolicyNotAttachableException
ReportGenerationLimitExceededException = exceptions.ReportGenerationLimitExceededException
ServiceFailureException = exceptions.ServiceFailureException
ServiceNotSupportedException = exceptions.ServiceNotSupportedException
UnmodifiableEntityException = exceptions.UnmodifiableEntityException
UnrecognizedPublicKeyEncodingException = exceptions.UnrecognizedPublicKeyEncodingException
