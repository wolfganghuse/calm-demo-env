cd /var/www/html
echo "create database \`phpipam\`;" | sudo mysql -u root -p@@{mariadb_rootpwd}@@
mysql -u root -p@@{mariadb_rootpwd}@@ phpipam < db/SCHEMA.sql
echo "GRANT ALL on \`phpipam\`.* to phpipam@localhost identified by 'phpipamadmin';;" | sudo mysql -u root -p@@{mariadb_rootpwd}@@