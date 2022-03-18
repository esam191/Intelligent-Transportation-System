from kafka import KafkaProducer;
import json;
import time
import io;
from avro.io import DatumWriter, BinaryEncoder
import avro.schema
import numpy as np;

data=json.load(open('cred.json'))
bootstrap_servers=data['bootstrap_servers'];
sasl_plain_username=data['Api key'];
sasl_plain_password=data['Api secret'];
 
with open("ontarioTech.jpg", "rb") as f:
    value = f.read();
        
producer = KafkaProducer(bootstrap_servers=bootstrap_servers,security_protocol='SASL_SSL',sasl_mechanism='PLAIN',\
    sasl_plain_username=sasl_plain_username,sasl_plain_password=sasl_plain_password,key_serializer=lambda v: v.encode())
producer.send('Images', value,key='OntarioTech');
producer.close();
