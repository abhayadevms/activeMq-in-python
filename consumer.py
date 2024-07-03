import stomp

class Consumer(stomp.ConnectionListener):
    def __init__(self, host, port, queue):
        self.conn = stomp.Connection([(host,port)])
        self.conn.set_listener('', self)
        # self.conn.start()
        self.conn.connect('admin', 'password', wait=True)
        self.conn.subscribe(destination=queue, id=1, ack='auto')

    def on_message(self, frame):
        priority = frame.headers.get('priority', 'N/A')
        print(f"Received message with priority {priority}: {frame.body}")

    def close(self):
        self.conn.disconnect()

# Example usage
if __name__ == "__main__":
    consumer = Consumer('localhost', 61613, '/queue/priority_queue')
    input("Press Enter to exit...\n")
    consumer.close()
