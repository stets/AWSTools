import boto3
import random, string
from multiprocessing import Process

#
# A tool to benchmark DynamoDB. Creates random strings of characters and writes them to the specified table. 
#
#define the connection
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('tablegoeshere')

def randomWriter():
    randomString = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
    table.put_item(Item={'id': randomString})
    print "Writing " + randomString  + " to DynamoDB table "


# holder function for calling multi-threading goodness
def scheduler():
    while True:
        randomWriter()


# do multithreading stuff. create 3 processes and start all
p1 = Process(target=scheduler)
p1.start()
p2 = Process(target=scheduler)
p2.start()
p3 = Process(target=scheduler)
p3.start()
p1.join()
p2.join()
p3.join()
