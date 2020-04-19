# Octoprint-PSU-Control-Hardware-Switch

I wanted a way to turn my printer on while I was at the printer in a manner that the PSU Control plugin would still function normally. 
These are some simple scripts I created that take input from a pushbutton switch connected to the Raspberry Pi GPIO pins.

Operation is simple.  The main script listener.py is run from rc.local.  When the button is pressed listener.py calls PSUOn.sh which uses
curl to send a command to PSUControl.  As I have PSUControl setup to automatically turn off after 10 minutes that the printer is idle,
PSUOff is not currently called from listener.py but it's a simple edit to implement power off. I'll implement this when I have more time.

Each button press is logged in /var/log/OctoPiPowerBtn/py_script.log. If you have some problems with this feature make sure the folder and file are created and check owner.
```bash
mkdir /var/log/OctoPiPowerBtn/
touch /var/log/OctoPiPowerBtn/py_script.log
chown -R pi:pi /var/log/OctoPiPowerBtn/
```

For this project to work, you have to copy vars.sh.dist to vars.sh and edit it with your OctoPrint API Key.