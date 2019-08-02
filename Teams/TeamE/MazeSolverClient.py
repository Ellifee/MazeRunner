"""
This class is the template class for the MQTT client which receives MQTT messages 
and sends MQTT messages
"""
import paho.mqtt.client as mqtt
import time
import array as arr
import os
from MazeSolverAlgoTemplate import MazeSolverAlgoTemplate

if "MQTTSERVER" in os.environ and os.environ['MQTTSERVER']:
    mqtt_server = os.environ['MQTTSERVER']
else:
    mqtt_server = "127.0.0.1"

# HINT: it might be a good idea to copy this file into your team folder, e.g. TeamA
# HINT: it might be good idea to rename both the file and the class name
class MazeSolverClient:

    # initialize the MQTT client
    def __init__(self,master):
        # TODO: this is you job now :-)

        print("Constructor Sample_MQTT_Publisher")
        self.master=master

        # HINT: here you should register the onConnect and onMessage callback functions
        #       it might be a good idea to look into file Framework\Test\test_mqtt_publisher.py
        self.master.on_connect=self.onConnect
        self.master.on_message=self.onMessage
        self.master.connect(mqtt_server,1883,60)

        self.solver = MazeSolverAlgoTemplate()
        
        # This MQTT client forwards the requests, so you need a link to the solver
        # HINT: don't forget to create your algorithm class here, e.g.
        #self.solver = MazeSolverAlgoTemplate()
        #pass

    # Implement MQTT publishing function
    def publish(self, topic, message=None, qos=0, retain=False):
        # TODO: this is you job now :-)
        # HINT: it might be a good idea to look into file Framework\Test\test_mqtt_publisher.py
        pass


    # Implement MQTT receive message function
    def onMessage(self, master, obj, msg):
        # TODO: this is you job now :-)
        # HINT: it might be a good idea to look into file Framework\Test\test_mqtt_subscriber.py
        topic = msg.topic
        payload = msg.payload.decode("utf-8"))
        print("TEAM_TEMPLATE: Received message:",  str(topic) , " --> " , str(payload)
        
        if topic=="/maze":
            if payload == "clear":
                self.solver.clearMaze()
            elif payload == "start":
                self.solver.startMaze()
            elif payload == "end":
                self.solver.endMaze()
                self.solver.printMaze()
        elif topic=="/maze/dimCols":
            self.solver.setDimCols(int(topic))
        elif topic=="/maze/dimRow":
            self.solver.setDimRows(int(topic))




    # Implement MQTT onConnecr function
    def onConnect(self, master, obj, flags, rc):
        self.master.subscribe("/maze" )
        self.master.subscribe("/maze/dimRow" )
        self.master.subscribe("/maze/dimCol" )
        self.master.subscribe("/maze/startCol" )
        self.master.subscribe("/maze/startRow" )
        self.master.subscribe("/maze/endCol" )
        self.master.subscribe("/maze/endRow" )
        self.master.subscribe("/maze/blocked" )
          
        # TODO: this is you job now :-)
        # HINT: it might be a good idea to look into file Framework\Test\test_mqtt_subscriber.py
        

    # Initiate the solving process of the maze solver
    def solveMaze(self):
        # TODO: this is you job now :-)

        #HINT:  don't forget to publish the results, e.g. 
        #self.publish("/maze/go" , resultString)
        pass

    
if __name__ == '__main__':
    mqttclient=mqtt.Client()
    #HINT: maybe you rename the MazeSolverAlgoTemplate class ?
    solverClient = MazeSolverClient(mqttclient)
    solverClient.master.loop_forever()
