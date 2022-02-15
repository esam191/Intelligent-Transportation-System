from kafka.admin import KafkaAdminClient, NewTopic


admin_client = KafkaAdminClient(bootstrap_servers=["localhost:9093","localhost:9094","localhost:9095"])

topic_list = NewTopic(name="cloud", num_partitions=3, replication_factor=3)

admin_client.create_topics([topic_list])

print ("Successfull created topic name: cloud")