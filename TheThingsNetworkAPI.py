import paho.mqtt.client as mqtt
import base64
import json

server = "eu.thethings.network"
up_topic = '+/devices/+/up'
user = "kasteel_hoensbroek_poc" #Application ID
password = "ttn-account-v2.sqQH7ZPQNPdvXmmAxa3ip1rKsYFCvsjB2SkPtFPRrys" #Application Acess Key


file = open("kasteelhoensbroekpoc.txt","w")
file.write("uitlezen data")
file.close()



def on_message(mqttc, obj, msg):
        m = str(msg.payload,'utf-8')
        m = json.loads(m)
        import pprint
        pprint.pprint(m)

        message =base64.b64decode(m['payload_raw'])
        data = int.from_bytes(message,byteorder='little')/100
        print("data = {}".format(data))
        json_object = json.dumps(m, indent = 4)
        # Writing to sample.json
        with open("kasteelhoensbroekpoc.txt", "a") as outfile:
                outfile.write(json_object)
                outfile.close(json_object)

mqttc = mqtt.Client()
mqttc.username_pw_set(user,password)
mqttc.on_message = on_message
mqttc.connect(server, 1883, 60)
mqttc.subscribe(up_topic, 0)

mqttc.loop_forever()
