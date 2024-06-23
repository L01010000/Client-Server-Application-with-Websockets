# WebSocket Client-Server Application

A WebSocket client-server application in Python demonstrating real-time bidirectional communication between a client (laptop) and a server (Raspberry Pi).

![GitHub repo size](https://img.shields.io/github/repo-size/your_username/your_repository)
![GitHub license](https://img.shields.io/github/license/your_username/your_repository)

---

## Table of Contents

- [Description](#description)
- [Key Features](#key-features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

---

## Description

This project sets up a WebSocket server on a Raspberry Pi that allows multiple clients to connect and exchange messages. Messages sent from any client are broadcasted to all connected clients by the server. The client (laptop) interacts with the server by sending messages and receiving messages broadcasted from other clients.

---

## Key Features

- **WebSocket Communication**: Real-time messaging between client and server using WebSocket protocol.
- **JSON Message Format**: Messages are exchanged in JSON format for easy parsing and serialization.
- **Colored Console Output**: Both client and server scripts provide colored output for improved readability and debugging.

---

## Requirements

- Python 3.x
- `websockets` library (`pip install websockets`)
- `colorama` library (`pip install colorama`)

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your_username/your_repository.git
   cd your_repository
