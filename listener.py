# Listener for PSUControl Plugin Hardware Switch
# Put this script in the ~pi/Switch directory.
# Add the following line to /etc/rc.local right before the line that says "exit 0"
# ~pi/oprint/bin/python ~pi/Switch/listener.py
#
# terry.bogayong@mak3rhq.com 

import RPi.GPIO as GPIO
import time
import os

#adjust for where your switch is connected
buttonPin = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

while True:
  # I'm ignoring bounce
  if (GPIO.input(buttonPin)):
    #Script to call when button is pressed
    os.system("sudo ~pi/Switch/PSUOn.sh")
    
