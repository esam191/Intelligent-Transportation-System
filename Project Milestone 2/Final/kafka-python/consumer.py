from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'topic_1',
    bootstrap_servers= ["localhost:9093","localhost:9094","localhost:9095"],
    auto_offset_reset = 'earliest',
    enable_auto_commit = True,
    group_id = 'test',
    )

print("Listening for messages...")

for message in consumer:
    print ("The topic is %s and The message is %s" % (message.topic, message.value))