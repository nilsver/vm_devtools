#!/bin/bash

ENV_FILE="/etc/vm_devtools/.env"
mkdir -p /etc/vm_devtools

if [ -f "$ENV_FILE" ]; then
    read -p "Configuration file '$ENV_FILE' already exists. Overwrite? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Aborting setup."
        exit 0
    fi
fi

read -p "Enter vmware username: " VM_USERNAME
read -p "Enter vmware password: " VM_PASSWORD
read -p "Enter vmware ip: " VM_IP
read -p "Enter your main VM name: " VM_MAIN

{
  echo "VM_USERNAME=$VM_USERNAME"
  echo "VM_PASSWORD=$VM_PASSWORD"
  echo "VM_IP=$VM_IP"
  echo "VM_MAIN=$VM_MAIN"
} > "$ENV_FILE"

chmod 600 "$ENV_FILE"

echo "Configuration saved to $ENV_FILE"
