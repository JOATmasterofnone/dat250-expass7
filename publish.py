import pika
import time

# Establish a connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue='task_queue'm durable=True)

# Initialize a counter
counter = 1

while True:
    message = f"Hello World {counter}"
    
    # Publish the message to the queue
    channel.basic_publish(exchange='', routing_key='task_queue', body=message)

    print(f" [x] Sent '{message}'")
    
    # Increment the counter
    counter += 1

    # Wait for 10 seconds before sending the next message
    time.sleep(10)

# Close the connection
connection.close()

