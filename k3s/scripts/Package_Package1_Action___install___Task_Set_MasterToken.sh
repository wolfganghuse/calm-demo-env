#!/bin/bash

if [ @@{calm_array_index}@@ -ne 0 ];then
  exit
fi
sleep 10

echo "MasterToken=$(sudo cat /var/lib/rancher/k3s/server/node-token)"