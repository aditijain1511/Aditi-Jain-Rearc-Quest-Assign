from aws_cdk import (
    Stack,
    aws_s3 as s3,
    Duration,
    aws_sqs as sqs,
    aws_lambda as _lambda,
    aws_lambda_event_sources as lambda_event_sources,
    aws_s3_notifications as s3_notifications,
    aws_events as events,
    aws_events_targets as targets,
)
from constructs import Construct

class ExistingResourcesDataPipelineStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Import existing S3 bucket
        data_bucket = s3.Bucket.from_bucket_name(self, "ExistingBucket", "rerac-quest-s3-bucket")
        
        queue = sqs.Queue(
            self, "DataQueue",
            visibility_timeout=Duration.seconds(65)  # Lambda timeout is 60s, so we use 65s
        )

        # Add S3 event notification to SQS for JSON files only
        notification_filter = s3.NotificationKeyFilter(suffix=".json")
        data_bucket.add_event_notification(
            s3.EventType.OBJECT_CREATED,
            s3_notifications.SqsDestination(queue),
            notification_filter
        )

        # Import existing Part 3 Lambda function
        part3_lambda = _lambda.Function.from_function_arn(
            self, "data-analysis-rearc",
            "arn-lambda-part3"
        )

        # Add SQS event source to Part 3 Lambda
        part3_lambda.add_event_source(lambda_event_sources.SqsEventSource(queue))

        # Import existing Part 1 Lambda function
        part1_lambda = _lambda.Function.from_function_arn(
            self, "data-ingestion-rearc",
            "arn-lambda-part1"
        )

        # Schedule Part 1 Lambda to run daily at 6 AM UTC - 11.30 am ist
        rule = events.Rule(
            self, "DailyScheduleRule",
            schedule=events.Schedule.cron(minute="30", hour="8"),
        )
        rule.add_target(targets.LambdaFunction(part1_lambda))
