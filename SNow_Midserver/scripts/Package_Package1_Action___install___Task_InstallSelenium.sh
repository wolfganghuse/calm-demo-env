sudo yum install -y python3
sudo pip3 install selenium

sudo yum install -y firefox 
sudo yum install -y wget unzip zip
sudo yum install -y  glibc.i686
wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
tar -xvzf geckodriver-v0.26.0-linux64.tar.gz
sudo cp geckodriver /usr/local/bin/geckodriver

#echo "JAVA_HOME=/usr/lib/jvm/jre-1.8.0-openjdk" >> ~/.bash_profile java-1.8.0-openjdk.x86_64