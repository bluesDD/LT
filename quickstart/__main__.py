"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3

for a in range(2):
  # Create an AWS resource (S3 Bucket)
  bucket = s3.Bucket('hogehoge' + str(a))

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)
