#!/bin/bash
set -ex

# Install kubectl
curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl

# Create kubeconfig
mkdir ~/.kube
echo '@@{Kubernetes.KUBECONFIG}@@' | base64 --decode > ~/.kube/config

# Validate kubeconfig
kubectl version
kubectl get nodes