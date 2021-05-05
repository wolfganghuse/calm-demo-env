#!/bin/bash

if [ @@{calm_array_index}@@ -ne 0 ];then
  exit
fi
sleep 10

echo -n "kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
   name: acs-abs
provisioner: com.nutanix.csi
parameters:
   csiProvisionerSecretName: ntnx-secret
   csiProvisionerSecretNamespace: default
   csiNodePublishSecretName: ntnx-secret
   csiNodePublishSecretNamespace: default
   dataServiceEndPoint: @@{PrismElement_DataIP}@@
   storageContainer: @@{CSI_StorageContainer}@@
   fsType: @@{CSI_fsType}@@
   flashMode: DISABLED
reclaimPolicy: Delete" | tee ntnx-storageclass.yaml





echo -n "kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
   name: acs-abs
provisioner: com.nutanix.csi
parameters:
   csiProvisionerSecretName: ntnx-secret
   csiProvisionerSecretNamespace: default
   csiNodePublishSecretName: ntnx-secret
   csiNodePublishSecretNamespace: default
   dataServiceEndPoint: @@{PrismElement_DataIP}@@
   storageContainer: @@{CSI_StorageContainer}@@
   storageType: NutanixVolumes
   description: k3s-acs-abs
   fsType: @@{CSI_fsType}@@
   flashMode: DISABLED
reclaimPolicy: Delete" | tee ntnx-storageclass.yaml






kubectl create -f ntnx-storageclass.yaml