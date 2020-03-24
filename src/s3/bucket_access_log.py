import boto3
import logging

###################################################################################################
####  create a cloudwatch on s3 create bucket and set target to this lambda functions #####
###################################################################################################

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def set_access_log(bucket_name, account_number):
    s3 = boto3.client("s3")
    s3.put_bucket_logging(Bucket=bucket_name, BucketLoggingStatus={"LoggingEnabled": {
        "TargetBucket": "access-logs-bucket",
        'TargetPrefix': "/".join(["dev", account_number, bucket_name, ""])
    }})


def lambda_handler(event, context):
    logger.info("event " + str(event))
    event_details = event['detail']
    event_name = event_details['eventName']
    account_number = context.invoked_function_arn.split(":")[4]

    if event_name == 'CreateBucket':
        bucket_name = event_details['requestParameters']['bucketName']
        set_access_log(bucket_name, account_number)
