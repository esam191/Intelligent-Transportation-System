# environment variable setup for private key file
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=""

from google.cloud import pubsub_v1
import time
import json;
import io;

# TODO(developer)
project_id = ""
topic_id = ""

publisher = pubsub_v1.PublisherClient()
# The `topic_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/topics/{topic_id}`
topic_path = publisher.topic_path(project_id, topic_id)

file1 = open('../images.txt', 'r')

while True:
    line = file1.readline()
    if not line:
        break
    arr=line.split(":")
    value={'key':int(arr[0]),'image':arr[1][0:-1]};
    future = publisher.publish(topic_path, json.dumps(value).encode('utf-8'));
    print("Image with key "+arr[0]+" is sent")
    time.sleep(0.1);
