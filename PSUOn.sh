#!/bin/bash
# Put this in the ~pi/Switch directory
# You'll need to substitute your own values for:
#   - API key from your instance of Octoprint
#   - Username and password for logging into OctoPrint
#
# Questions? Email me at terry.bogayong@mak3rhq.command
source ~pi/Octoprint-PSU-Control-Hardware-Switch/vars.sh
curl -s -H "Content-Type: application/json" -H "X-Api-Key: $API_KEY" -X POST -d '{ "command":"turnPSUOn" }' http://localhost/api/plugin/psucontrol