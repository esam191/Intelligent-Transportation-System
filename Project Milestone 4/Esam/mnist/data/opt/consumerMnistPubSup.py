import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=""

from google.cloud import pubsub_v1

project_id = ""
subscription_id = ""

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_id)
import json
def callback(message: pubsub_v1.subscriber.message.Message) -> None:
    #print(f"Received {json.loads(message)}.")
    print(f"Received {json.loads(message.data)}.")
    message.ack()

streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print(f"Listening for messages on {subscription_path}..\n")

with subscriber:
    streaming_pull_future.result()