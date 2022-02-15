const Kafka = require("kafkajs").Kafka

run();
async function run(){
    try {

        const kafka = new Kafka({
            "clientId": "myapp",
            "brokers": ["localhost:9093","localhost:9094","localhost:9095"]
        })

        const admin = kafka.admin();
        console.log("Connecting...")

        await admin.connect()
        console.log("Connected!")
        
        await admin.createTopics({
            "topics": [{
                "topic": "topic2",
                "numPartitions": 2
            }]
        })

        console.log("Created successfully!")
        await admin.disconnect();

    } catch (error) {

        console.error(`An error has occured! ${error}`)

    } finally {
        process.exit(0);
    }
}