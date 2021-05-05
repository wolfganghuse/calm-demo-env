#!/bin/bash
set -ex

# Download karbonctl
sudo wget -O /usr/local/bin/karbonctl https://storage.googleapis.com/testdrive-templates/library/release/karbon/karbonctl
sudo chmod 775 /usr/local/bin/karbonctl