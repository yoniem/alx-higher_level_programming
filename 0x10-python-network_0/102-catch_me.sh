#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me to get the server to respond with the message "You got me!"

# Send request to cause the server to respond with the message.
curl -s -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me -L
