from kafka import KafkaProducer
import time

def main():
    bootstrap_servers = ['wn01.itversity.com:6667', 'wn02.itversity.com:6667']
    topicName = 'streaming_demo'

    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

    with open('json_data.txt', 'rb') as reader:
        for message in reader.readlines():
            time.sleep(3)
            ack = producer.send(topicName, message)

    metadata = ack.get()
    print(metadata.topic+"-"+str(metadata.partition))

if __name__ == '__main__':
    main()
