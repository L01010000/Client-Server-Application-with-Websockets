# WebSocket Server Application


This project sets up a WebSocket server on a Raspberry Pi that allows multiple clients to connect and exchange messages.

<img src="https://github.com/L01010000/Client-Server-Application-with-Websockets/blob/main/poc.png" width="800px" />

---

## How It Works

The server initializes a WebSocket server on a specified IP address (0.0.0.0) and port (12345). Once initialized, it begins listening for incoming WebSocket connections.

When a client connects:

The server adds the client's WebSocket connection to a set (connected_clients) to manage active connections.
It logs the connection event with a timestamp and client address.

Asynchronously listens for messages from connected clients.
Each incoming message is parsed as JSON:
If valid JSON>
Checks for a 'message' key within the JSON data.
Sends a confirmation message back to the sender upon successful message receipt.
If invalid JSON>
sends an error message indicating a format issue back to the sender.

Monitors for client disconnection events.
Removes disconnected clients from the connected_clients set and logs the event with a timestamp and client address.

---


## Key Features

- **WebSocket Communication**
- **JSON Message Format**
- **Colored Console Output**

---

## Requirements

- Python 3.x
- `websockets` library (`pip install websockets`)
- `colorama` library (`pip install colorama`)

## Enjoy
