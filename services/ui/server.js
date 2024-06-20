import express from "express";
import bodyParser from "body-parser";
import cors from "cors";
import kafka from "kafka-node";

const app = express();
const port = 5000;

app.use(bodyParser.json());
app.use(cors());

// Configurar o Producer do Kafka
const Producer = kafka.Producer;
const client = new kafka.KafkaClient({ kafkaHost: "localhost:9092" });
const producer = new Producer(client);

producer.on("ready", () => {
    console.log("Kafka Producer is connected and ready.");
});

producer.on("error", (error) => {
    console.error("Error in Kafka Producer:", error);
});

// Rota para enviar mensagem
app.post("/send", (req, res) => {
    const { message } = req.body;
    const payloads = [{ topic: "test-topic", messages: message, partition: 0 }];

    producer.send(payloads, (err, data) => {
        if (err) {
            res.status(500).send(err);
        } else {
            res.status(200).send(data);
        }
    });
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
