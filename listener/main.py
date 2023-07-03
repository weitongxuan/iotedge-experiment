from azure.iot.device import IoTHubDeviceClient, Message , IoTHubModuleClient
CONNECTION_STRING = "HostName=smartcity.azure-devices.net;DeviceId=test001;SharedAccessKey=75N18Hxe+QAmx6UFXIMvhtJdPKRU4s2LHG2RI3gHuXI="
DEVICE_ID = "test001"

def message_listener(message):
    print("接收到訊息: {}".format(message.data))

# 建立 IoT 設備客戶端

# client = IoTHubModuleClient.create_from_edge_environment()
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
# 設定訊息接收處理程序
client.on_message_received = message_listener

# 連線到 Azure IoT 中心
client.connect()
print("connected")

# 持續執行，直到程式被中斷
while True:
    pass

# 斷開連線
client.disconnect()