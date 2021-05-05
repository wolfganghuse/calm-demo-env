#!/bin/bash

if [ @@{calm_array_index}@@ -ne 0 ];then
  exit
fi

sleep 10

echo -n "apiVersion: v1
kind: Secret
metadata:
 name: ntnx-secret
 namespace: default
data:
 key: " | tee ntnx-secret.yaml
 echo -n "@@{PrismElement_IP}@@:@@{PrismElement_Port}@@:@@{PrismElement.username}@@:@@{PrismElement.secret}@@" | base64 | tee -a ntnx-secret.yaml
 
 kubectl create -f ntnx-secret.yaml