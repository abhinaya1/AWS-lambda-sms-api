from __future__ import print_function
import json
import boto3
print('Loading function')

def lambda_handler(event, context):
    boto3.client('sns').publish(
        MessageAttributes= {

                    'AWS.SNS.SMS.SMSType': {
                                                 'DataType': 'String',
                                                 'StringValue': 'Transactional'   
											}
					},
        PhoneNumber = event['PhoneNumber'],
        Message = event['Message']
    )
    return {'code': 0, 'Message': 'success'}