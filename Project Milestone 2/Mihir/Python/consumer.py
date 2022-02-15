from kafka import KafkaConsumer

TOPIC_NAME = 'cloud'

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=["localhost:9093", "localhost:9094", "localhost:9095"])

for message in consumer:
    print ("Topic= %s Value=%s" % (message.topic, message.value))


consumer.close()
