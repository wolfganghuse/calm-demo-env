sudo yum install -y docker-ce docker-ce-cli containerd.io
sudo groupadd docker
sudo usermod -aG docker ${USER}

sudo service docker start
sudo systemctl enable docker