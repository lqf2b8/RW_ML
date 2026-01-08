from quixstreams import Application


def produce_trades(
        kafka_broker_address: str,
        kafka_topic: str,
        product_id: str,
):
    """ 
    Reads trades from kraken websocket and produces them to a Kafka topic.

    Args:
        kafka_broker_address (str): Address of the Kafka broker.
        kafka_topic (str): Kafka topic to save trades to.
        product_id (str): Product ID to filter trades for.

        Returns:
            None
    """

    app = Application(broker_address=kafka_broker_address)

    topic = app.topic(name=kafka_topic, value_serializer="json")

    with app.get_producer() as producer:
        #kraken_trades_stream = app.get_data_streams().from_kraken_trades(product_id=product_id)
        #kraken_trades_stream.save_to_topic(producer=producer, topic=topic)

        while True:
            event = {
                "product_id": "ETH/USD",
                "price": 1000,
                "qty": 1,
                "timestamp_ms": 163000000000,
            }
            message = topic.serialize(key=event["product_id"], value=event)
            producer.produce(topic=topic.name, key=message.key, value=message.value)

            from time import sleep
            sleep(1)


if __name__ == "__main__":
    produce_trades(
        kafka_broker_address="localhost:19092",
        kafka_topic="trades",
        product_id="ETH/USD",
    )
