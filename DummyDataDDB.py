import boto.dynamodb2
from boto.dynamodb2.table import Table
from boto.dynamodb2.fields import HashKey
from boto.regioninfo import RegionInfo
from boto.dynamodb2.layer1 import DynamoDBConnection
from faker import Factory
import uuid
import time

try:
    sessions = Table(
        table_name='table_name',
        schema=[HashKey('schema')],
        connection=DynamoDBConnection(
        region=RegionInfo(name='resion',
                          endpoint='dynamodb.endpoint')
        ))

except:
    print("Dynamo can't connect")

def create_session():
    id = str(uuid.uuid4())
    timestamp = time.strftime("%Y%m%d%H%M%S")
    ipv4 = Factory.create().ipv4()
    users_id = Factory.create().slug()
    users_name = Factory.create().first_name()
    users_surname = Factory.create().last_name()
    res = sessions.put_item(data={
        'key': id#,
      #  'Name': users_name
    })


    #print 'Hash key: ' + id + ' {' + users_id + ',' + users_name + ',' + users_surname + ',' + str(ipv4) + ',' + timestamp + '} '
    #result = create_session()
    #print(result)

if __name__ == '__main__':

    for x in range(20000):
        create_session()
