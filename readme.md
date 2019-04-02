# dEC2line Serverless

## Description:
* serverless architecture to alert on idle/underutilized EC2 resources in AWS account environment
* contains:
  * A Lambda function attaching CloudWatch alarms on EC2 instances
  * A CloudWatch event monitoring change state of EC2 instance from stopped->running
  * A SNS topic sending email notifications based on CloudWatch alarms


## Usage:
* cloudformation template.yml should be configured and deployed into desired region
* configuration allows for
  * setting desired EC2 instance family to be monitored
  * setting desired count of maximum consecutive measurements failed triggering the alarm
  * setting desired utilization target that defines idle/underutilized state
  * setting desired email address that notifications will be delivered to (email distribution list is recommended here)
* desired email address subscription needs to be confirmed by acknowledgeing the registration email that is sent after successful deployment 
* every new EC2 instance that changes the state stopped->running will then trigger CloudWatch alarm, that then sends a notification into SNS topic, sending an email to specified recipient


## License and Warranty:
Copyright 2019, Miro Masat

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Credit:
Inspired by: https://medium.com/@Hironsan/save-aws-ec2-cost-by-automatically-stopping-idle-instance-using-lambda-and-cloudwatch-759edd62b27d

## Architecture: 

TBD

