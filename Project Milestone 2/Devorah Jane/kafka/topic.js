//const Kafka = require("kafkajs").Kafka
const {Kafka} = require("kafkajs")

run();

async function run(){
    try{
        const kafka = new Kafka({
            "clientID": "myapp",
            "brokers": [
                "localhost:9093",
                "localhost:9094",
                "localhost:9095"
            ]
        })

        const admin = kafka.admin()
        console.log("Connecting....")
        await admin.connect()
        console.log("Connected....")

        //A-M, N-Z
        await admin.createTopics({  // Create topics
            "topics":[{
                "topic": "Users",   //name
                "numPartitions": 2  //num of partition
            }]
        })

        console.log("Created successfully!")
        await admin.disconnect();

    }
    catch(ex){
        console.error(`Something bad happened ${ex}`)
    }
    finally{
        process.exit
    }
}