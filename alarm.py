#!/usr/bin/env python

# Control Lasermodule from Raspberry Pi
# https://raspberrytips.nl/laser-module-aansturen-via-gpio/

import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

# ----------------Laser Start-----------------------
LaserGPIO = 17 # --> PIN11/GPIO17


def setup():
    GPIO.setmode(GPIO.BCM)
    # GPIO.setwarnings(False)
    GPIO.setup(LaserGPIO, GPIO.OUT)
    GPIO.output(LaserGPIO, GPIO.HIGH)

def emergency():

    while 1:
        print 'Laser = on'
        GPIO.output(LaserGPIO, GPIO.LOW) # led on
        return "Emergency"

def eatingTime():
    while 1:
        print 'Laser=on'
        GPIO.output(LaserGPIO, GPIO.LOW) # led on
        time.sleep(3)
        print 'Laser=off'
        GPIO.output(LaserGPIO, GPIO.HIGH) # led off
        time.sleep(1)
        return "Eating Time"

def GoingToUSC():
    while 1:
        print 'Laser=on'
        GPIO.output(LaserGPIO, GPIO.LOW) # led on
        time.sleep(1.5)
        print 'Laser=off'
        GPIO.output(LaserGPIO, GPIO.HIGH) # led off
        time.sleep(1.0)

def Paging():
    while 1:
        print 'Laser=on'
        GPIO.output(LaserGPIO, GPIO.HIGH) # led on
        time.sleep(1.5)
        print 'Laser=off'
        GPIO.output(LaserGPIO, GPIO.LOW) # led off
        time.sleep(1.0)

def destroy():
    GPIO.output(LaserGPIO, GPIO.LOW)
# ----------------Laser End-----------------------

# ================  MQTT  ========================
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
   
    client.subscribe("Emergency")
    # client.subscribe("EatingTime")


def on_message(client, userdata, msg):
    if(msg.topic == "Emergency"):
        print(msg.topic+" "+str(emergency()))
    elif(msg.topic == "EatingTime"):
        print(msg.topic+" "+str(eatingTime()))
    elif(msg.topic == "GoingToUSC"):
        GoingToUSC()
    elif(msg.topic == "Paging"):
        destroy()
    elif(msg.topic == "Off"):
        destroy()


client = mqtt.Client()
client.on_message = on_message
client.on_connect = on_connect

client.connect("test.mosquitto.org", 1883,60)

if __name__ == '__main__':
    setup()

client.loop_forever()
# =================================================


