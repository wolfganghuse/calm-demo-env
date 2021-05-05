#!/bin/bash

if [ @@{calm_array_index}@@ -ne 0 ];then
  exit
fi

kubectl delete node @@{k3s_service.Node2Remove}@@