import boto3
import logging


###################################################################################################
####  create a cloudwatch on s3 create bucket and set target to this lambda functions #####
###################################################################################################
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def add_tags(bucket_name, user):
    tags_set = [{"creator", user}]
    s3 = boto3.resource("s3")
    s3.put_bucket_tagging(bucket_name).put(Tagging={"TagSet", tags_set})


def lambda_handler(event, context):
    logger.info("event " + str(event))
    event_details = event['detail']
    event_name = event_details['eventName']
    principal_id = event_details['userIdentity']['principalId']
    user_type = event_details['userIdentity']['type']
    user = ""
    if user_type == 'IAMUser':
        user = event_details['userIdentity']['userName']
    else:
        user = principal_id.split(":")[1]  # for assume this returns email id

    if event_name == 'CreateBucket':
        bucket_name = event_details['requestParameters']['bucketName']
        add_tags(bucket_name, user)
