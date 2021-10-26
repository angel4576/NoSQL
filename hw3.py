
import boto3


s3 = boto3.resource('s3',
 aws_access_key_id='AKIAQA2QXNO4OJ7JQUZG',
 aws_secret_access_key='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'
)

try:
 s3.create_bucket(Bucket='cs1660-bucket-zirui', CreateBucketConfiguration={
 'LocationConstraint': 'us-west-2'})
except Exception as e:
 print (e)

 bucket = s3.Bucket("cs1660-bucket-zirui")
 
 bucket.Acl().put(ACL='public-read')
 #upload a file
body = open('D:\python\laugh.jpg', 'rb')

o = s3.Object('cs1660-bucket-zirui', 'test').put(Body=body )

s3.Object('cs1660-bucket-zirui', 'test').Acl().put(ACL='public-read')


dyndb = boto3.resource('dynamodb',
 region_name='us-west-2',
 aws_access_key_id='AKIAQA2QXNO4OJ7JQUZG',
 aws_secret_access_key='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'
)

try:
 table = dyndb.create_table(
 TableName='DataTable2',
 KeySchema=[
 {
 'AttributeName': 'Id',
 'KeyType': 'HASH'
 },
 {
 'AttributeName': 'Temp',
 'KeyType': 'RANGE'
 }
 ],
 AttributeDefinitions=[
 {
 'AttributeName': 'Id',
 'AttributeType': 'S'
 },
 {
 'AttributeName': 'Temp',
 'AttributeType': 'S'
 },
 ],
 ProvisionedThroughput={
 'ReadCapacityUnits': 5,
 'WriteCapacityUnits': 5
 }
 )
except Exception as e:
 print (e)
 #if there is an exception, the table may already exist. if so...
 table = dyndb.Table("DataTable2")
 
 #wait for the table to be created
table.meta.client.get_waiter('table_exists').wait(TableName='DataTable2')

print(table.item_count)
0

import csv

with open('D:\\cs1660\\hw3\\experiments.csv', 'r') as csvfile:
 csvf = csv.reader(csvfile, delimiter=',', quotechar='|')
 for item in csvf:
    print (item)
    if(item[0] != "\ufeffId"):
        body = open('D:\\cs1660\\hw3\\datafiles\\'+item[4], 'rb')
        #body = open(item[4], 'rb')
        
        s3.Object('cs1660-bucket-zirui', item[4]).put(Body=body )
        md = s3.Object('cs1660-bucket-zirui', item[4]).Acl().put(ACL='public-read')
        url = "https://s3-us-west-2.amazonaws.com/cs1660-bucket-zirui/"+item[4]
        metadata_item = {'Id': item[0], 'Temp': item[1], 
                'Conductivity' : item[2], 'Concentration' : item[3], 'URL': item[4], 'url':url} 
        try:
            table.put_item(Item=metadata_item)
        except:
            print ("item may already be there or another failure")
 

 response = table.get_item(
    Key = {
        'Id': '1',
        'Temp': '-1'
    }
 )
 item = response['Item']
 print(item)
 




