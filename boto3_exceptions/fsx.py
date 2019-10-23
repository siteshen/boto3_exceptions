import boto3

exceptions = boto3.client('fsx').exceptions

ActiveDirectoryError = exceptions.ActiveDirectoryError
BackupInProgress = exceptions.BackupInProgress
BackupNotFound = exceptions.BackupNotFound
BackupRestoring = exceptions.BackupRestoring
BadRequest = exceptions.BadRequest
FileSystemNotFound = exceptions.FileSystemNotFound
IncompatibleParameterError = exceptions.IncompatibleParameterError
InternalServerError = exceptions.InternalServerError
InvalidExportPath = exceptions.InvalidExportPath
InvalidImportPath = exceptions.InvalidImportPath
InvalidNetworkSettings = exceptions.InvalidNetworkSettings
MissingFileSystemConfiguration = exceptions.MissingFileSystemConfiguration
NotServiceResourceError = exceptions.NotServiceResourceError
ResourceDoesNotSupportTagging = exceptions.ResourceDoesNotSupportTagging
ResourceNotFound = exceptions.ResourceNotFound
ServiceLimitExceeded = exceptions.ServiceLimitExceeded
UnsupportedOperation = exceptions.UnsupportedOperation
