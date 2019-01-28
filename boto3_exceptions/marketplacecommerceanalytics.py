import boto3

exceptions = boto3.client('marketplacecommerceanalytics').exceptions

MarketplaceCommerceAnalyticsException = exceptions.MarketplaceCommerceAnalyticsException
