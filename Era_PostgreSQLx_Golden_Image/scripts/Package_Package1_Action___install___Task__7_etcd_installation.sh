#pip based installation
sudo pip install etcd3==0.10.0
 
pip show etcd3

etcd --version

# rpm install
wget https://rpmfind.net/linux/centos/7/extras/x86_64/Packages/etcd-3.3.11-2.el7.centos.x86_64.rpm
 
sudo rpm -i etcd-3.3.11-2.el7.centos.x86_64.rpm

etcd --version