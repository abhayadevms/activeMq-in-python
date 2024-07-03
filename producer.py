import stomp

class Producer:
    def __init__(self, host, port, queue):
        self.conn = stomp.Connection([(host, port)])
        # self.conn.start()
        self.conn.connect('admin', 'password', wait=True)
        self.queue = queue

    def send_message(self, message, priority):
        self.conn.send(body=message, destination=self.queue, headers={'priority': priority})

    def close(self):
        self.conn.disconnect()

# Example usage
if __name__ == "__main__":
    producer = Producer('localhost', 61613, '/queue/priority_queue')
    producer.send_message('High priority message', 9)
    producer.send_message('Medium priority message', 5)
    producer.send_message('Low priority message', 1)
    producer.close()
