import boto3, os

def put_cpu_alarm(instance_id):
                cloudWatch   = boto3.client('cloudwatch')
                cloudWatch.put_metric_alarm(
                    AlarmName          = 'CPU_ALARM_'+instance_id,
                    AlarmDescription   = 'Alarm when CPU of '+os.environ['ALARM_INSTANCE']+' does not exceed '+os.environ['ALARM_TRESHOLD']+'%',
                    AlarmActions       = [os.environ['SNS_ARN']],
                    MetricName         = 'CPUUtilization',
                    Namespace          = 'AWS/EC2' ,
                    Statistic          = 'Average',
                    Dimensions         = [{'Name': 'InstanceId', 'Value': instance_id}],
                    Period             = 300,
                    EvaluationPeriods  = int(os.environ['ALARM_EVALUATION_PERIODS']),
                    Threshold          = int(os.environ['ALARM_TRESHOLD']),
                    ComparisonOperator = 'LessThanOrEqualToThreshold',
                    TreatMissingData   = 'notBreaching'
                )


def lambda_handler(event, context):
                instance_id = event['detail']['instance-id']
                ec2 = boto3.resource('ec2')
                instance = ec2.Instance(instance_id)
                if instance.instance_type.startswith(os.environ['ALARM_INSTANCE']):
                    put_cpu_alarm(instance_id)