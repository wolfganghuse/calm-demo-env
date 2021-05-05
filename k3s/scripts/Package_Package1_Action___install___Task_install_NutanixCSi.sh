#!/bin/bash

if [ @@{calm_array_index}@@ -ne 0 ];then
  exit
fi

wget http://download.nutanix.com/csi/v1.0.1/csi-v1.0.1.tar.gz
tar xvf csi-v1.0.1.tar.gz
kubectl create -f CSI/ntnx-csi-rbac.yaml
kubectl create -f CSI/ntnx-csi-attacher.yaml
kubectl create -f CSI/ntnx-csi-node.yaml
kubectl create -f CSI/ntnx-csi-provisioner.yaml

