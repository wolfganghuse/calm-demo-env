if systemctl list-units --type=service | grep -Fq 'firewalld'; then   
  sudo firewall-cmd --add-service=http
  sudo firewall-cmd --add-service=https
  sudo firewall-cmd --runtime-to-permanent
fi
