import asyncio
import websockets
import json
from datetime import datetime
from colorama import Fore, Style, init

init()

connected_clients = set()

async def handler(websocket, path):
    connected_clients.add(websocket)
    client_address = websocket.remote_address
    print(f"{Fore.GREEN}[{datetime.now()}] New client connected: {client_address}{Style.RESET_ALL}")

    try:
        async for message in websocket:
            try:
                print(f"{Fore.YELLOW}[{datetime.now()}] Raw message received: {message}{Style.RESET_ALL}")
                data = json.loads(message)
                
                if isinstance(data, dict):
                    if 'message' in data:
                        print(f"{Fore.CYAN}[{datetime.now()}] Parsed message from {client_address}: {data['message']}{Style.RESET_ALL}")
                        
                        broadcast_message = json.dumps({"message": data['message']})
                        await asyncio.wait([client.send(broadcast_message) for client in connected_clients if client != websocket])
                    
                    confirmation_message = json.dumps({"confirmation": "Message received"})
                    await websocket.send(confirmation_message)
                else:
                    print(f"{Fore.CYAN}[{datetime.now()}] Parsed JSON data from {client_address}: {data}{Style.RESET_ALL}")
                    
                    confirmation_message = json.dumps({"confirmation": "Data received"})
                    await websocket.send(confirmation_message)

            except json.JSONDecodeError:
                print(f"{Fore.RED}[{datetime.now()}] Failed to decode JSON message: {message}{Style.RESET_ALL}")
                error_message = json.dumps({"error": "Invalid JSON format"})
                await websocket.send(error_message)

    except websockets.exceptions.ConnectionClosed:
        print(f"{Fore.RED}[{datetime.now()}] Client disconnected: {client_address}{Style.RESET_ALL}")
    finally:
        connected_clients.remove(websocket)

async def main():
    server = await websockets.serve(handler, "0.0.0.0", 12345)
    print(f"{Fore.GREEN}[{datetime.now()}] Server started on ws://0.0.0.0:12345{Style.RESET_ALL}")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
