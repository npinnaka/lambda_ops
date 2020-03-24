import boto3
import logging

###################################################################################################
####  create a cloudwatch on s3 create bucket and set target to this lambda functions #####
###################################################################################################
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def set_default_encryption(bucket_name):
    s3 = boto3.client("s3")
    s3.put_bucklet_encryption(Bucket=bucket_name,
                              ServerSideEncryptionConfiguration={
                                  'Rules': [
                                      {
                                          'ApplyServerSideEncryptionByDefault': {
                                              'SSEAlgorithm': 'AES256'
                                          }
                                      }
                                  ]
                              })


def lambda_handler(event, context):
    logger.info("event " + str(event))
    event_details = event['detail']
    event_name = event_details['eventName']
    if event_name == 'CreateBucket':
        bucket_name = event_details['requestParameters']['bucketName']
        set_default_encryption(bucket_name)
