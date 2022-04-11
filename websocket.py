
# import asyncio
# import websockets

# ws_url = "ws://127.0.0.1:8000/ws/ac/"

# async def command_receiver():
#     async with websockets.connect(ws_url) as websocket:
#         while True:
#             # message = await websocket.recv()
#             # await websocket.send("Received the command '{message}'")
#             await websocket.send(" sendddd ")
#             print(await websocket.recv())


#             # if message == "start":
#             #     # run the start command
#             #     ...
#             # elif message == "stop":
#             #     # run the stop command
#             #     ...
#             # else:
#             #     await websocket.send("Unknown command")     


# asyncio.get_event_loop().run_until_complete(command_receiver())


import asyncio
import json
import websockets

async def hello():
    async with websockets.connect("ws://127.0.0.1:8000/ws/ac/tally/") as websocket:

        await websocket.send(json.dumps({
            
                'message': 'database',
                'username': 'ankit',
                'room': 'tally'
            }));  
        
        while True:
            print(await websocket.recv())

asyncio.run(hello())