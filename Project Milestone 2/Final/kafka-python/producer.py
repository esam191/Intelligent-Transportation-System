from kafka import KafkaProducer

try:
    producer = KafkaProducer(
        bootstrap_servers= ["localhost:9093","localhost:9094","localhost:9095"],
        )

    producer.send('topic_1', b'Esam test message 2')
    producer.send( 'topic_1', key=b'message-one', value=b'Kafka-Python testing 2')

    print("Sent message successfully!")
    producer.close()
except:
    print("An error has occured!")

