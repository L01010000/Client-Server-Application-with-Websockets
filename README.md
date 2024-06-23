<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WebSocket Client-Server Application</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        h1, h2, h3 {
            color: #333;
        }
        code {
            background-color: #f0f0f0;
            padding: 2px 5px;
            border-radius: 4px;
            font-family: Consolas, monospace;
        }
        pre {
            background-color: #f8f8f8;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            white-space: pre-wrap;
        }
        .badge {
            display: inline-block;
            font-size: 0.8em;
            font-weight: bold;
            color: #fff;
            background-color: #007bff;
            padding: 4px 8px;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <h1>WebSocket Client-Server Application</h1>

    <p>A simple WebSocket client-server application in Python, where the client (laptop) sends messages to the server (Raspberry Pi), and the server broadcasts these messages to all connected clients.</p>

    <div>
        <span class="badge">GitHub repo size</span>
        <span class="badge">GitHub license</span>
    </div>

    <h2>Description</h2>

    <p>This project demonstrates how to set up a WebSocket server on a Raspberry Pi and connect to it from a client running on a laptop. Messages sent from the client are broadcasted to all connected clients by the server.</p>

    <h2>Key Features</h2>
    <ul>
        <li>WebSocket Communication: Real-time bidirectional communication between client and server.</li>
        <li>JSON Message Format: Messages are exchanged in JSON format for easy parsing and serialization.</li>
        <li>Colorful Console Output: Client and server scripts provide colored output for better readability and debugging.</li>
    </ul>

    <h2>Requirements</h2>
    <ul>
        <li>Python 3.x</li>
        <li><code>websockets</code> library (<a href="https://pypi.org/project/websockets/">installation instructions</a>)</li>
        <li><code>colorama</code> library (<a href="https://pypi.org/project/colorama/">installation instructions</a>)</li>
    </ul>

    <h2>Installation</h2>
    <ol>
        <li>Clone the repository:</li>
        <pre><code>git clone https://github.com/your_username/your_repository.git<br>cd your_repository</code></pre>
        
        <li>Install dependencies:</li>
        <pre><code>pip install -r requirements.txt</code></pre>
    </ol>

    <h2>Usage</h2>
    <ol>
        <li><strong>Start the Server (Raspberry Pi):</strong></li>
        <pre><code>python3 server.py</code></pre>

        <li><strong>Run the Client (Laptop):</strong></li>
        <pre><code>python3 client.py</code></pre>

        <li><strong>Interaction:</strong></li>
        <ul>
            <li>The client connects to the server and sends messages.</li>
            <li>The server receives messages and broadcasts them to all connected clients.</li>
            <li>Messages are displayed with timestamps and in colored format for clarity.</li>
        </ul>
    </ol>

    <h2>License</h2>
    <p>This project is licensed under the <a href="LICENSE">MIT License</a> - see the LICENSE file for details.</p>

</body>
</html>
