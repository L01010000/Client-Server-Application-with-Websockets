WebSocket Client-Server Application
A simple WebSocket client-server application in Python, where the client (laptop) sends messages to the server (Raspberry Pi), and the server broadcasts these messages to all connected clients.



Description
This project demonstrates how to set up a WebSocket server on a Raspberry Pi and connect to it from a client running on a laptop. Messages sent from the client are broadcasted to all connected clients by the server.

Key Features
WebSocket Communication: Real-time bidirectional communication between client and server.
JSON Message Format: Messages are exchanged in JSON format for easy parsing and serialization.
Colorful Console Output: Client and server scripts provide colored output for better readability and debugging.
Requirements
Python 3.x
websockets library (pip install websockets)
colorama library (pip install colorama)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your_username/your_repository.git
cd your_repository
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Start the Server (Raspberry Pi):

bash
Copy code
python3 server.py
Run the Client (Laptop):

bash
Copy code
python3 client.py
Interaction:

The client connects to the server and sends messages.
The server receives messages and broadcasts them to all connected clients.
Messages are displayed with timestamps and in colored format for clarity.
