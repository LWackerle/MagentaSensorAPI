import sys
import paho.mqtt.client as mqtt
from api_manager import API_Manager
import json

# initialize api

api = API_Manager("http://api:8000/")

# initiate client
client = mqtt.Client('test')

# define callback


def on_message(client, userdata, message):
    payload = json.loads(message.payload.decode("utf-8"))
    dev_id = payload["dev_id"]
    occupied = None
    gateway = None

    if "metadata" in payload and "gateways" in payload["metadata"]:
        gateway = payload["metadata"]["gateways"][0]["gtw_id"]
    else:
        gateway = "test"

    if payload["payload_fields"]["occupied"] == 48:
        occupied = False
    elif payload["payload_fields"]["occupied"] == 49:
        occupied = True

    api.update_device_status(dev_id, occupied)
    api.add_to_history(dev_id, occupied, gateway)


def on_connect(client, userdata, flags, rc):
    print('Connected to TTN:', rc)
    # subscribtion
    client.subscribe("magentadesktestsetup/devices/+/up")
    print('Subscribed to uplink of devices for magentadesksetup')


client.on_connect = on_connect
client.on_message = on_message


# set credentials TTN
client.username_pw_set('magentadesktestsetup',
                       password='ttn-account-v2.O1YWpxbTkL0r3E9q2Eu-PyghSeiW_E1tfF-hLDr-v2g')

# connect TTN
client.connect('eu.thethings.network')

client.loop_forever()
