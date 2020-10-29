import paho.mqtt.client as mqtt

# initiate client
client = mqtt.Client('test')

# define callback
def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)

def on_connect(client, userdata, flags, rc):
    print('Connected to TTN:', rc)
    # subscribtion
    client.subscribe("magentadesktestsetup/devices/+/up")
    print('Subscribed')

client.on_connect = on_connect
client.on_message = on_message


# set credentials TTN
client.username_pw_set('magentadesktestsetup', password='ttn-account-v2.O1YWpxbTkL0r3E9q2Eu-PyghSeiW_E1tfF-hLDr-v2g')

# connect TTN
client.connect('eu.thethings.network')

client.loop_forever()