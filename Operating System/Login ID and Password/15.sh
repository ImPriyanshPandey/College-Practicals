#!/bin/bash

# Accept login name from user
read -p "Enter login name : " login_name

# Check if login name exists
if getent passwd "$login_name" > /dev/null; then
echo "Login name '$login_name' is valid."
else
echo "Entered login name '$login_name' is invalid."
fi