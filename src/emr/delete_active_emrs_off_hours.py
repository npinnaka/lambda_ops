import boto3
import logging

###################################################################################################
####  create a con schedular in cloudwatch for a spefic time of the day to terminate emr clusters ####
###################################################################################################
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    emr = boto3.client("emr")
    emr_response = emr.list_clusters(ClusterStates=[
        'STARTING', 'BOOTSTRAPPING', 'RUNNING', 'WAITING'
    ])

    clusters = list(cluster['Id'] for cluster in emr_response['Clusters'])
    if clusters:
        logger.info("terminating clusters "+ str(clusters))
        emr.set_termination_protection(JobFlowIds=clusters, TerminationProtected=False)
        emr.terminate_job_flows(JobFlowIds=clusters)
    else:
        logger.info("no clusters found")
