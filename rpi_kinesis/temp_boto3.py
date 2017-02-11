import boto3

client = boto3.client('firehose')
client.list_delivery_streams()

r = {'Data':b'{"temp:8100.8"}'}

client.put_record(DeliveryStreamName='testStream', Record=r)