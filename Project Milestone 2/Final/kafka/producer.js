const Kafka = require("kafkajs").Kafka
const msg = process.argv[2]

run();
async function run(){
    try {

        const kafka = new Kafka({
            "clientId": "myapp",
            "brokers": ["localhost:9093","localhost:9094","localhost:9095"]
        })

        const producer = kafka.producer();
        console.log("Connecting...")

        await producer.connect()
        console.log("Connected!")

        const result = await producer.send({
            "topic": "topic2",
            "messages": [
                {
                    "value": msg
                }
            ]
        })

        console.log(`Sent successfully! ${JSON.stringify(result)}`)
        await producer.disconnect();

    } catch (error) {

        console.error(`An error has occured! ${error}`)

    } finally {
        process.exit(0);
    }
}