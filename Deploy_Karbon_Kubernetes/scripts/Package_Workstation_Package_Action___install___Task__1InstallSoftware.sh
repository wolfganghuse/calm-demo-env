#!/bin/bash
set -ex

sudo yum -y update
sudo yum -y install vim jq git wget elinks

echo "alias k=kubectl" | tee -a ~/.bash_profile