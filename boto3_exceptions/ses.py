import boto3

exceptions = boto3.client('ses').exceptions

AccountSendingPausedException = exceptions.AccountSendingPausedException
AlreadyExistsException = exceptions.AlreadyExistsException
CannotDeleteException = exceptions.CannotDeleteException
ConfigurationSetAlreadyExistsException = exceptions.ConfigurationSetAlreadyExistsException
ConfigurationSetDoesNotExistException = exceptions.ConfigurationSetDoesNotExistException
ConfigurationSetSendingPausedException = exceptions.ConfigurationSetSendingPausedException
CustomVerificationEmailInvalidContentException = exceptions.CustomVerificationEmailInvalidContentException
CustomVerificationEmailTemplateAlreadyExistsException = exceptions.CustomVerificationEmailTemplateAlreadyExistsException
CustomVerificationEmailTemplateDoesNotExistException = exceptions.CustomVerificationEmailTemplateDoesNotExistException
EventDestinationAlreadyExistsException = exceptions.EventDestinationAlreadyExistsException
EventDestinationDoesNotExistException = exceptions.EventDestinationDoesNotExistException
FromEmailAddressNotVerifiedException = exceptions.FromEmailAddressNotVerifiedException
InvalidCloudWatchDestinationException = exceptions.InvalidCloudWatchDestinationException
InvalidConfigurationSetException = exceptions.InvalidConfigurationSetException
InvalidDeliveryOptionsException = exceptions.InvalidDeliveryOptionsException
InvalidFirehoseDestinationException = exceptions.InvalidFirehoseDestinationException
InvalidLambdaFunctionException = exceptions.InvalidLambdaFunctionException
InvalidPolicyException = exceptions.InvalidPolicyException
InvalidRenderingParameterException = exceptions.InvalidRenderingParameterException
InvalidS3ConfigurationException = exceptions.InvalidS3ConfigurationException
InvalidSNSDestinationException = exceptions.InvalidSNSDestinationException
InvalidSnsTopicException = exceptions.InvalidSnsTopicException
InvalidTemplateException = exceptions.InvalidTemplateException
InvalidTrackingOptionsException = exceptions.InvalidTrackingOptionsException
LimitExceededException = exceptions.LimitExceededException
MailFromDomainNotVerifiedException = exceptions.MailFromDomainNotVerifiedException
MessageRejected = exceptions.MessageRejected
MissingRenderingAttributeException = exceptions.MissingRenderingAttributeException
ProductionAccessNotGrantedException = exceptions.ProductionAccessNotGrantedException
RuleDoesNotExistException = exceptions.RuleDoesNotExistException
RuleSetDoesNotExistException = exceptions.RuleSetDoesNotExistException
TemplateDoesNotExistException = exceptions.TemplateDoesNotExistException
TrackingOptionsAlreadyExistsException = exceptions.TrackingOptionsAlreadyExistsException
TrackingOptionsDoesNotExistException = exceptions.TrackingOptionsDoesNotExistException
