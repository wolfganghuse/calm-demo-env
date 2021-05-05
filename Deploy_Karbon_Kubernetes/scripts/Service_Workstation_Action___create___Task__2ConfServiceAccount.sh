#!/bin/bash
set -ex
ACCOUNT=workstation
cd ~/
kubectl create serviceaccount $ACCOUNT
cat << EOF > $ACCOUNT-rb.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: $ACCOUNT-rolebinding
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- kind: ServiceAccount
  name: $ACCOUNT
  namespace: default
EOF
kubectl create -f $ACCOUNT-rb.yaml
TOKEN=$(kubectl get secrets $(kubectl get serviceaccounts $ACCOUNT -o jsonpath={.secrets[].name}) -o jsonpath={.data.token} | base64 --decode)
CLUSTER=$(kubectl config view --minify -o jsonpath='{.clusters[].name}')
kubectl config set-credentials $ACCOUNT --token=$TOKEN
kubectl config set-context $ACCOUNT-context --cluster $CLUSTER --user $ACCOUNT
kubectl config use-context $ACCOUNT-context

#sed "s/    token:.*/    token: `kubectl get secrets $(kubectl get serviceaccounts workstation -o jsonpath={.secrets[].name}) -o jsonpath={.data.token} | base64 --decode`/g" ~/.kube/config > ~/.kube/configsa
#mv ~/.kube/config ~/.kube/tokenconfig
#mv ~/.kube/configsa ~/.kube/config