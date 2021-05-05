#!/bin/bash
set -ex

# Install helm
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3
chmod 700 get_helm.sh
sh get_helm.sh

# Validate install
helm version
helm search hub wordpress

# Configure repos
# helm repo add stable https://kubernetes-charts.storage.googleapis.com
helm repo add stable https://charts.helm.sh/stable
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update