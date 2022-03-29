import time
import json;
import io;
from kafka import KafkaProducer

data=json.load(open('cred.json'))
bootstrap_servers=data['bootstrap_servers'];
sasl_plain_username=data['Api key'];
sasl_plain_password=data['Api secret'];

producer = KafkaProducer(bootstrap_servers=bootstrap_servers,security_protocol='SASL_SSL',sasl_mechanism='PLAIN',\
    sasl_plain_username=sasl_plain_username,sasl_plain_password=sasl_plain_password,\
    value_serializer=lambda m: json.dumps(m).encode('utf-8'))
    
file1 = open('images.txt', 'r')

while True:
    line = file1.readline()
 
    if not line:
        break
    arr=line.split(":")
    value={'key':int(arr[0]),'image':arr[1][0:-1]};
    producer.send('mnist_image', value);
    print("Image with key "+arr[0]+" is sent")
    time.sleep(0.1);
producer.close();
