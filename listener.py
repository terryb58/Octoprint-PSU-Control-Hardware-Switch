# Listener for PSUControl Plugin Hardware Switch
# Put this script in the ~pi/Switch directory.
# Add the following line to /etc/rc.local right before the line that says "exit 0"
# ~pi/oprint/bin/python ~pi/Switch/listener.py
#
# terry.bogayong@mak3rhq.com 

import RPi.GPIO as GPIO
import os
import time
import datetime
import signal

#Button Pin
buttonPin = 27
#Log file location
logFile = "/var/log/OctoPiPowerBtn/py_script.log"

try:
  #GPIO Initialisation
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

  #Callback executed when button pressed
  def my_callback(channel):
    start_time = time.time()

    #wait untill button released
    while GPIO.input(channel) == 1:
      pass

    buttonTime = time.time() - start_time

    #if button pressed for at least .2 of a second (avoid false detections)
    if buttonTime >= .2:
      os.system("sudo ~pi/Octoprint-PSU-Control-Hardware-Switch/PSUToggle.sh")
  
      try:
        os.mkdir("/var/log/OctoPiPowerBtn")
      except OSError:
        pass

      try:
        f = open(logFile, "x")
      except:
        f = open(logFile, "a")

      f.write(datetime.datetime.now().strftime("%X-%m-%d %H:%M:%S.%f") + " Btn pressed\n")
      f.close()
      
    start_time = 0
    buttonTime = 0

  #GPIO interrupt to detect button press
  GPIO.add_event_detect(buttonPin, GPIO.RISING, callback=my_callback, bouncetime=300)

  #Make script running forever
  signal.pause()

except KeyboardInterrupt:
  GPIO.cleanup()

#Clean GPIO port on exit
GPIO.cleanup()