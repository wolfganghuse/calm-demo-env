sudo yum -y install mod_ssl
sudo mkdir /etc/ssl/private
sudo chmod 700 /etc/ssl/private
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt -subj "/C=DE/ST=NRW/L=Dortmund/O=Sales/CN=phpipam"
sudo openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048
cat /etc/ssl/certs/dhparam.pem | sudo tee -a /etc/ssl/certs/apache-selfsigned.crt
sudo sed -i 's/SSLCertificateFile \/etc\/pki\/tls\/certs\/localhost.crt/SSLCertificateFile \/etc\/ssl\/certs\/apache-selfsigned.crt/g' /etc/httpd/conf.d/ssl.conf
sudo sed -i 's/SSLCertificateKeyFile \/etc\/pki\/tls\/private\/localhost.key/SSLCertificateKeyFile \/etc\/ssl\/private\/apache-selfsigned.key/g' /etc/httpd/conf.d/ssl.conf
sudo sed -i 's/#ServerName www.example.com:443/ServerName phpipam:443/g' /etc/httpd/conf.d/ssl.conf
sudo systemctl restart httpd.service
#sudo firewall-cmd --add-service=http
#sudo firewall-cmd --add-service=https
#sudo firewall-cmd --runtime-to-permanent