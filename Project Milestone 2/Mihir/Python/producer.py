from kafka import KafkaProducer

def withoutpartation():
    try:
        TOPIC_NAME = 'cloud'
        KAFKA_SERVER = ["localhost:9093", "localhost:9094", "localhost:9095"]
        
       #producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER) 
        producer = KafkaProducer(bootstrap_servers=["localhost:9093", "localhost:9094", "localhost:9095"])
        producer.send(TOPIC_NAME, b'Mihir')
        producer.send(TOPIC_NAME, key=b'message-two', value=b'cloud computing Milestone 2')
        print("Sent successfully!") 
        producer.close() 
    except:
        print("Exception occured")

userInput = input("Do you want partition? Y or N \n")

if (userInput.upper() == "N"):
    withoutpartation()

if (userInput.upper() == "Y"):
    withoutpartation()
