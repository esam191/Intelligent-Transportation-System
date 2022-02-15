const Kafka = require("kafkajs").Kafka


run();
async function run(){
    try {

        const kafka = new Kafka({
            "clientId": "myapp",
            "brokers": ["localhost:9093","localhost:9094","localhost:9095"]
        })

        const consumer = kafka.consumer({"groupId": "test"});
        console.log("Connecting...")

        await consumer.connect()
        console.log("Connected!")

        //await consumer.disconnect();

        consumer.subscribe({
            "topic": "topic2",
            "fromBeginning": true
        })

        await consumer.run({
            "eachMessage": async result => {
                console.log(`Received Message ${result.message.value}`)
            }
        })

    } catch (error) {

        console.error(`An error has occured! ${error}`)

    }
}