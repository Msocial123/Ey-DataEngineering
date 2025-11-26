import boto3
import time

glue = boto3.client("glue")
emr = boto3.client("emr")
athena = boto3.client("athena")
# ses = boto3.client("ses")

def wait_for_glue(job_name, run_id):
    while True:
        status = glue.get_job_run(JobName=job_name, RunId=run_id)["JobRun"]["JobRunState"]
        print(job_name, status)
        if status in ["SUCCEEDED", "FAILED", "STOPPED"]:
            return status
        time.sleep(200)

def lambda_handler(event, context):

    ##############################
    # 1. RUN GLUE ETL JOBS
    ##############################
    glue_jobs = [
        "users_etl_job",
        "products_etl_job",
        "transactions_etl_job",
        "clickstream_etl_job"
    ]

    print("Starting Glue ETL Jobs...")
    for job in glue_jobs:
        res = glue.start_job_run(JobName=job)
        print(f"Started: {job}, RunID: {res['JobRunId']}")
        wait_for_glue(job, res["JobRunId"])
    print("All Glue jobs completed!")

    ##############################
    # 2. RUN EMR SPARK STEP
    ##############################
    print("Starting EMR Step...")

    response = emr.add_job_flow_steps(
        JobFlowId="j-RRYHBXUBJ6DV",
        Steps=[
            {
                "Name": "Transaction Analytics",
                "ActionOnFailure": "CONTINUE",
                "HadoopJarStep": {
                    "Jar": "command-runner.jar",
                    "Args": [
                        "spark-submit",
                        "s3://murali-20-retail/scripts/transaction_emr_load.py"
                    ]
                }
            }
        ]
    )
    print("EMR Step Submitted:", response["StepIds"][0])

    ##############################
    # 3. RUN ATHENA QUERY
    ##############################
    print("Running Athena Query...")

    athena_res = athena.start_query_execution(
        QueryString="SELECT * FROM daily_revenue LIMIT 20;",
        QueryExecutionContext={"Database": "ecommerce"},
        ResultConfiguration={
            "OutputLocation": "s3://murali-20-retail/athena_results/"
        }
    )

    print("Athena Query ID:", athena_res["QueryExecutionId"])

    # ##############################
    # # 4. SEND EMAIL
    # ##############################
    # ses.send_email(
    #     Source="muraliclahan526@gmail.com",
    #     Destination={"ToAddresses": ["muraliclahan526@gmail.com"]},
    #     Message={
    #         "Subject": {"Data": "Pipeline Completed"},
    #         "Body": {
    #             "Text": {
    #                 "Data": "Pipeline executed successfully!"
    #             }
    #         }
    #     }
    # )

    return {"message": "Pipeline executed successfully"}
