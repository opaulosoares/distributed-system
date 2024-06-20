import React, { useState } from "react";
import axios from "axios";

const KafkaProducer = () => {
    const [message, setMessage] = useState("");

    const sendMessage = async () => {
        try {
            const response = await axios.post("http://localhost:5000/send", {
                message,
            });
            console.log("Message sent:", response.data);
        } catch (error) {
            console.error("Error sending message:", error);
        }
    };

    return (
        <div>
            <h2>Kafka Producer</h2>
            <input
                type="text"
                value={message}
                onChange={(e) => setMessage(e.target.value)}
            />
            <button onClick={sendMessage}>Send Message</button>
        </div>
    );
};

export default KafkaProducer;
