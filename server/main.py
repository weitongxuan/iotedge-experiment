from fastapi import FastAPI
from azure.iot.device import IoTHubDeviceClient, Message , IoTHubModuleClient, MethodResponse
import uvicorn
print("starting")

client = IoTHubModuleClient.create_from_edge_environment()


client = IoTHubDeviceClient.create_from_connection_string("")
client.get_storage_info_for_blob()

def method_request_handler(method_request):
    
    print( "{} : {}".format(method_request.name, payload=method_request.payload))

    response_payload = {"Response": "Direct method {} reveived".format(method_request.name)}
    response_status = 200

    method_response = MethodResponse.create_from_method_request(method_request, response_status, response_payload)
    client.send_method_response(method_response)





client.on_method_request_received = method_request_handler

client.connect()
print("connected iothub")

app = FastAPI()
result = 0
@app.get("/add")
def add():

    global result
    result = result +1 
    client.patch_twin_reported_properties({
        "current_count" : result
    })
    return {"result": result }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)