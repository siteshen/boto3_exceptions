import boto3

exceptions = boto3.client('s3').exceptions

BucketAlreadyExists = exceptions.BucketAlreadyExists
BucketAlreadyOwnedByYou = exceptions.BucketAlreadyOwnedByYou
NoSuchBucket = exceptions.NoSuchBucket
NoSuchKey = exceptions.NoSuchKey
NoSuchUpload = exceptions.NoSuchUpload
ObjectAlreadyInActiveTierError = exceptions.ObjectAlreadyInActiveTierError
ObjectNotInActiveTierError = exceptions.ObjectNotInActiveTierError
