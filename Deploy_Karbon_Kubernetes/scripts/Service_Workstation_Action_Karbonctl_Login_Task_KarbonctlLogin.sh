#!/bin/bash
set -ex

# Run the karbonctl login command
karbonctl login --pc-username @@{PC_Creds.username}@@ --pc-password @@{PC_Creds.secret}@@ --pc-ip @@{Kubernetes.PC_IP}@@