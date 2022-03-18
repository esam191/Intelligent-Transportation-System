from kafka import KafkaConsumer;
import json;
import time
import io;
from avro.io import DatumReader, BinaryDecoder
import avro.schema

group_id=None;
data=json.load(open('cred.json'))
bootstrap_servers=data['bootstrap_servers'];
sasl_plain_username=data['Api key'];
sasl_plain_password=data['Api secret'];

schema = avro.schema.parse(open("./schema.avsc").read())
reader = DatumReader(schema)

def decode(msg_value):
    message_bytes = io.BytesIO(msg_value)
    message_bytes.seek(5)
    decoder = BinaryDecoder(message_bytes)
    event_dict = reader.read(decoder)
    return event_dict

consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers,security_protocol='SASL_SSL',sasl_mechanism='PLAIN',\
    sasl_plain_username=sasl_plain_username,sasl_plain_password=sasl_plain_password,auto_offset_reset='earliest',\
    consumer_timeout_ms=1000,group_id=group_id,value_deserializer=lambda m: decode(m),\
    key_deserializer=lambda m: str(json.loads(m)) if m is not None else '')

consumer.subscribe(['myDBtest'])

while True:
    for message in consumer:
        if message is not None:
            print('partition:'+str(message.partition)+"\nkey:"+message.key+"\nvalue:",'');
            print(message.value,'')
            print("\n--------\n");
        time.sleep(0.1);
consumer.close()
