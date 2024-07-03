## activeMq

## Prerequisites

- ActiveMQ server
- Python 3.x
- Required Python libraries: `stomp.py`

## Setup Instructions

### Install Required Libraries

```bash
pip install stomp.py 
```
Clone the repository:
```bash
git clone https://github.com/abhayadevms/activeMq-in-python.git
```

Start ActiveMQ and other services using Docker Compose:
Ensure Docker and Docker Compose are installed on your system. Start the services defined in docker-compose.yml:

```bash
docker-compose up -d
```

#### Run the Producer:
Use the producer.py script to send messages:
```bash
python producer.py
```
#### Run the Consumer:
Use the consumer.py script to consume messages from the ActiveMQ:
```bash
python consumer.py
```

## ActiveMQ Management UI
To monitor and manage the ActiveMQ server, open your web browser and navigate to:
```bash
http://localhost:8161
```
Log in with the default credentials:

```bash
Username: admin
Password: password
```
