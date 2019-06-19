#!/bin/bash
# Put this in the ~pi/Switch directory
# You'll need to substitute your own values for:
#   - API key from your instance of Octoprint
#   - Username and password for logging into OctoPrint
curl -s -H "Content-Type: application/json" -H "X-Api-Key: __YOUR_API_KEY_FROM_OCTOPRINT__" -X POST -d '{ "command":"turnPSUOff" }' -u username:password http://localhost/api/plugin/psucontrol
