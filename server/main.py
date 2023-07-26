from fastapi import FastAPI
from azure.iot.device import IoTHubDeviceClient, MethodResponse , IoTHubModuleClient ,MethodRequest
import uvicorn, logging, time

logging.basicConfig(level=logging.INFO)

print("starting")

def method_received(req: MethodRequest  ):
    print("{}:{}".format(req.name, req.payload))
    response_payload = {"Response": "OK"}
    response_status = 200 
    method_response = MethodResponse.create_from_method_request(req, response_status, response_payload)
    client.send_method_response(method_response)


def received_desire(twinData):
    print(twinData)

def connection_state_changed():
    print("state is : {}".format(client.connected))  
    if client.connected:
        twin = client.get_twin()
        print(twin)

client = IoTHubModuleClient.create_from_edge_environment()
client.on_method_request_received = method_received
client.on_twin_desired_properties_patch_received = received_desire
client.on_connection_state_change = connection_state_changed

client.connect()

while not client.connected:
    time.sleep(1)

print("connected iothub")
connection_state_changed()

app = FastAPI()
result = 0


@app.get("/add")
def add():

    global result
    result = result +1 
    client.patch_twin_reported_properties( {
        "current_count" : result
    })
    client.send_message(result)
    return {"result": result }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)