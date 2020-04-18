import paho.mqtt.client as mqtt
import base64
import json
import pprint

server = "eu.thethings.network"
up_topic = '+/devices/+/up'
user = "kasteel_hoensbroek_poc" #Application ID
password = "ttn-account-v2.sqQH7ZPQNPdvXmmAxa3ip1rKsYFCvsjB2SkPtFPRrys" #Application Acess Key

def on_message(mqttc, obj, msg):
    
    m = str(msg.payload,'utf-8')
    m = json.loads(m)    
    pprint.pprint(m)

message =base64.b64decode(m['payload_raw'])
data = int.from_bytes(message,byteorder='little')/100
print("Data = {}".format(data))

mqttc = mqtt.Client()
mqttc.username_pw_set(user,password)
mqttc.on_message = on_message
mqttc.connect(server, 1883, 60)
mqttc.subscribe(up_topic, 0)

mqttc.loop_forever()
