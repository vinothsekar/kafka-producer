from kafka import KafkaProducer


def main():
    bootstrap_servers = ['wn01.itversity.com:6667', 'wn02.itversity.com:6667']
    topicName = 'streaming_demo'

    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

    ack = producer.send(topicName, b'Hello World!!!!!!!!')

    metadata = ack.get()
    print(metadata.topic)
    print(metadata.partition)
    print("python main function")


if __name__ == '__main__':
    main()
