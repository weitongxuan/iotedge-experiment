import logging
from azure.eventhub import EventHubConsumerClient, EventData ,CheckpointStore

connection_str = 'Endpoint=sb://iothub-ns-smartcity-25123052-7222bd878a.servicebus.windows.net/;SharedAccessKeyName=iothubowner;SharedAccessKey=H6JBFYEk5X61mpFqZdSSZOUTF8Mz6OiVLYcrVDKgTlc=;EntityPath=smartcity'
consumer_group = 'simon'
eventhub_name = 'smartcity'
client = EventHubConsumerClient.from_connection_string(connection_str, consumer_group, eventhub_name=eventhub_name)

logger = logging.getLogger("azure.eventhub")
# logging.basicConfig(level=logging.INFO)

def on_event(partition_context, event: EventData ):
    print("Received event: {}".format(event.body_as_str()))
    partition_context.update_checkpoint(event)



with client:
    print("ready")
    client.receive(
        on_event=on_event,
        
    )