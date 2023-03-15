import asyncio
from typing import List
from json import loads
from src.heavy.service import calculate_factorial
from fastapi import FastAPI, APIRouter, WebSocket, WebSocketDisconnect
from concurrent.futures.process import ProcessPoolExecutor

app = FastAPI(
    title='Test for Optimacros'
)

router = APIRouter(
    tags=['Heavy']
)

app.include_router(router)


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def send_personal_json(self, message: str, websocket: WebSocket):
        await websocket.send_json(loads(message))


manager = ConnectionManager()


@app.on_event("startup")
async def on_startup():
    app.state.executor = ProcessPoolExecutor(max_workers=2)


@app.on_event("shutdown")
async def on_shutdown():
    app.state.executor.shutdown()


@app.websocket("/ws/factorial/")
async def websocket_factorial(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            value = None
            try:
                value = int(loads(data).get('request_factorial'))
                if value < 0:
                    raise ValueError("Only positive integers are allowed")
            except:
                result = 'Error. The value must be a positive integer'
            else:
                loop = asyncio.get_event_loop()
                result = await loop.run_in_executor(app.state.executor, calculate_factorial, value)
                result = 'error while calculating' if not result else result
            send_data = f'{{"request_factorial": "{value}", "result": "{result}"}}'
            await manager.send_personal_json(send_data, websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
