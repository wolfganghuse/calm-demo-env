sudo yum -y install epel-release

#After install Please verify the version (min 7.11)
yum info epel-release

#pip Install
 
sudo yum -y install python-pip
 
sudo pip install --upgrade "pip < 21"

#Check pip version (min 19.01) 
pip --version