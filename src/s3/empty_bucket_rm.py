import boto3
def empty_and_delete_bucket(bucket_name):
    s3 = boto3.resource("s3")
    bucket_response = s3.Bucket(bucket_name)
    bucket_response.objects.delete();
    bucket_response.delete()


