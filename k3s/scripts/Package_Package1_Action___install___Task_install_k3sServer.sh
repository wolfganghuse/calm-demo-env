#!/bin/bash

if [ @@{calm_array_index}@@ -ne 0 ];then
  exit
fi
sleep 10

sudo curl -sfL https://get.k3s.io | sh -s - --write-kubeconfig-mode 644

###Wait until K3s is up and running...

sleep 60
#kubectl version
#while [ $? -ne 0 ]; do
#	sleep 5
#    kubectl version
#done
