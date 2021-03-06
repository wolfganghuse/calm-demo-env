sudo yum update -y
sudo yum install -y wget unzip git

TER_VER=`curl -s https://api.github.com/repos/hashicorp/terraform/releases/latest |  grep tag_name | cut -d: -f2 | tr -d \"\,\v | awk '{$1=$1};1'`
wget https://releases.hashicorp.com/terraform/${TER_VER}/terraform_${TER_VER}_linux_amd64.zip

unzip terraform_${TER_VER}_linux_amd64.zip
sudo mv terraform /usr/local/bin/

rm terraform_${TER_VER}_linux_amd64.zip

terraform version
