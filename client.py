import asyncio
import websockets
import json
from datetime import datetime
from colorama import Fore, Style, init

init()

async def receive_messages(websocket):
    while True:
        try:
            response = await websocket.recv()
            data = json.loads(response)
            print(f"{Fore.BLUE}[{datetime.now()}] < Received:{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{data['message']}{Style.RESET_ALL}")
        except websockets.exceptions.ConnectionClosed:
            print(f"{Fore.RED}[{datetime.now()}] Connection closed{Style.RESET_ALL}")
            break

async def send_messages(websocket):
    while True:
        message = input("Enter a message: ")
        data = {"message": message}
        await websocket.send(json.dumps(data))
        print(f"{Fore.GREEN}[{datetime.now()}] > Sent:{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{data['message']}{Style.RESET_ALL}")

async def hello():
    uri = "ws://192.168.11.54:12345"
    async with websockets.connect(uri) as websocket:
        print(f"{Fore.GREEN}[{datetime.now()}] Connected successfully to {uri}{Style.RESET_ALL}")
        receive_task = asyncio.create_task(receive_messages(websocket))
        await send_messages(websocket)
        await receive_task

if __name__ == "__main__":
    try:
        asyncio.run(hello())
    except KeyboardInterrupt:
        exit()
