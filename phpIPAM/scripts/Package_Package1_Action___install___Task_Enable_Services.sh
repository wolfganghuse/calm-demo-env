sudo service httpd start
sudo chkconfig httpd on
sudo firewall-cmd --permanent --add-port=80/tcp
sudo service mariadb start
sudo chkconfig mariadb on
mysqladmin --user=root password "@@{mariadb_rootpwd}@@"
