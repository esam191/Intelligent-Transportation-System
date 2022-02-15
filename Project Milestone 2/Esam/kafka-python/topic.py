from kafka.admin import KafkaAdminClient, NewTopic

topics = []

admin = KafkaAdminClient(
    bootstrap_servers=['localhost:9093','localhost:9094','localhost:9095'], 
    client_id='myapp'
)

topics.append(
    NewTopic(
        name="topic_1", 
        num_partitions=3, 
        replication_factor=3
        )
    )

admin.create_topics(
    new_topics=topics
    )

print("Topic created successfully!")