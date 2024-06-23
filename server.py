import asyncio
import websockets
import json
from datetime import datetime
from colorama import Fore, Style, init

init()

connected_clients = set()

async def handler(websocket, path):
    connected_clients.add(websocket)
    print(f"{Fore.GREEN}[{datetime.now()}] New client connected: {websocket.remote_address}{Style.RESET_ALL}")
    try:
        async for message in websocket:
            data = json.loads(message)
            print(f"{Fore.BLUE}[{datetime.now()}] Received message from {websocket.remote_address}:{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{data['message']}{Style.RESET_ALL}")
            for client in connected_clients:
                if client != websocket:
                    await client.send(json.dumps(data))
    except websockets.exceptions.ConnectionClosed:
        print(f"{Fore.RED}[{datetime.now()}] Client disconnected: {websocket.remote_address}{Style.RESET_ALL}")
    finally:
        connected_clients.remove(websocket)

async def main():
    async with websockets.serve(handler, "0.0.0.0", 12345):
        print(f"{Fore.YELLOW}[{datetime.now()}] Server started on ws://0.0.0.0:12345{Style.RESET_ALL}")
        await asyncio.Future()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        exit()
