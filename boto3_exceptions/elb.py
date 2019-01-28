import boto3

exceptions = boto3.client('elb').exceptions

LoadBalancerNotFound = exceptions.LoadBalancerNotFound
CertificateNotFound = exceptions.CertificateNotFound
DependencyThrottle = exceptions.DependencyThrottle
DuplicateLoadBalancerName = exceptions.DuplicateLoadBalancerName
DuplicateListener = exceptions.DuplicateListener
DuplicatePolicyName = exceptions.DuplicatePolicyName
DuplicateTagKeys = exceptions.DuplicateTagKeys
InvalidConfigurationRequest = exceptions.InvalidConfigurationRequest
InvalidInstance = exceptions.InvalidInstance
InvalidScheme = exceptions.InvalidScheme
InvalidSecurityGroup = exceptions.InvalidSecurityGroup
InvalidSubnet = exceptions.InvalidSubnet
ListenerNotFound = exceptions.ListenerNotFound
LoadBalancerAttributeNotFound = exceptions.LoadBalancerAttributeNotFound
OperationNotPermitted = exceptions.OperationNotPermitted
PolicyNotFound = exceptions.PolicyNotFound
PolicyTypeNotFound = exceptions.PolicyTypeNotFound
SubnetNotFound = exceptions.SubnetNotFound
TooManyLoadBalancers = exceptions.TooManyLoadBalancers
TooManyPolicies = exceptions.TooManyPolicies
TooManyTags = exceptions.TooManyTags
UnsupportedProtocol = exceptions.UnsupportedProtocol
