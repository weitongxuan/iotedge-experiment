from fastapi import FastAPI
from azure.iot.device import IoTHubDeviceClient, Message , IoTHubModuleClient
import uvicorn
print("starting")
def message_listener(message):
    print("接收到訊息: {}".format(message.data))
client = IoTHubModuleClient.create_from_edge_environment()
client.on_method_request_received 

client.connect()
print("connected iothub")

app = FastAPI()
result = 0
@app.get("/add")
def add():
    global result
    result = result +1 
    return {"result": result }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)