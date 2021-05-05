cd /var/www/html/
sudo git clone https://github.com/phpipam/phpipam.git .
sudo git checkout 1.4
sudo chown apache:apache -R /var/www/html/
sudo chcon -t httpd_sys_content_t /var/www/html/ –R
sudo find . -type f -exec chmod 0644 {} \;
sudo find . -type d -exec chmod 0755 {} \;
sudo cp config.dist.php config.php