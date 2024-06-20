import React from "react";
import Header from "../components/Header/Header";
import ItemsTable from "../components/ItemsTable/ItemsTable";
import { Link } from "react-router-dom";
import TemplatePage from "./TemplatePage";
import KafkaProducer from "../components/KafkaProducer/KafkaProducer";

const Home = () => {
    const products = [
        {
            name: 'Apple iMac 27"',
            category: "PC",
            brand: "Apple",
            description:
                "What is a product description? A product description describes a product.",
            price: "$2999",
            dropdownId: "apple-imac-27-dropdown",
        },
        {
            name: 'Apple iMac 20"',
            category: "PC",
            brand: "Apple",
            description:
                "What is a product description? A product description describes a product.",
            price: "$1499",
            dropdownId: "apple-imac-20-dropdown",
        },
        // ... other products
    ];
    return (
        <TemplatePage>
            <h1>teste</h1>
            <KafkaProducer />
        </TemplatePage>
    );
};

export default Home;
