from kafka import KafkaProducer
from json import dumps

producer = KafkaProducer(
   value_serializer=lambda m: dumps(m).encode('utf-8'),
   bootstrap_servers=['localhost:9093', 'localhost:9093', 'localhost:9094']
)

producer.send("test", value={"hello": "producer"})