sudo yum install -y python-devel
sudo yum install -y python3-devel

sudo yum install --downloadonly --downloaddir=. iptables-services
sudo rpm -ivh iptables-services-1.4.21-35.el7.x86_64.rpm
sudo systemctl start iptables
sudo ln -s /usr/local/bin/patroni /usr/bin/patroni 


# Install the repository RPM:
sudo yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm

# Install PostgreSQL:
# Small fix for 9.6 Path and 96 Package
version="@@{postgre_version}@@"
sudo yum install -y postgresql${version//./}-devel
sudo yum install -y postgresql${version//./}-server
sudo yum install -y postgresql-libs

sudo pip3 install psycopg2-binary
sudo pip install urllib3==1.24.2