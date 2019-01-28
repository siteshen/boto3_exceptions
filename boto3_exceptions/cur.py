import boto3

exceptions = boto3.client('cur').exceptions

DuplicateReportNameException = exceptions.DuplicateReportNameException
InternalErrorException = exceptions.InternalErrorException
ReportLimitReachedException = exceptions.ReportLimitReachedException
ValidationException = exceptions.ValidationException
