"""
pipeline.py
----------------
This file launches BOTH producer and consumer using Python threads to simulate
a real streaming pipeline.

"""

import threading
from queue import Queue
from producer import CSVProducer
from consumer import Consumer

def main():
    """
    TODO:
    - Create the shared queue.
    - Instantiate the producer and consumer.
    - Create a thread for each.
    - Start both threads.
    - join them so the program runs continuously.


    The students should run:
        python pipeline.py
    and observe live streaming behavior.
    """
    q = Queue()
    CSV_PATH = "transactions.csv"  # Update this path to your CSV file
    
    producer = CSVProducer(CSV_PATH, q)
    producer_thread = threading.Thread(target=producer.start)
    producer_thread.start()

    consumer = Consumer(q)
    consumer_thread = threading.Thread(target=consumer.start)
    consumer_thread.start()
    



if __name__ == "__main__":
    print("Starting the Python Streaming Pipeline...")
    main()
