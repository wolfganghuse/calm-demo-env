#!/bin/bash
set -ex

if [ @@{calm_array_index}@@ -eq 0 ];then
	exit
fi

sudo curl -sfL https://get.k3s.io | K3S_TOKEN=@@{calm_array_MasterToken}@@ K3S_URL=https://@@{calm_array_address[0]}@@:6443 sh -
