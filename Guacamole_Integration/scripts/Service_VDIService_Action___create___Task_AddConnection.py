
# Set  headers
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
payload = '{"parentIdentifier":"@@{calm_array_GroupIdentifier}@@","name":"@@{name}@@","protocol":"rdp","parameters":{"port":"","read-only":"","swap-red-blue":"","cursor":"","color-depth":"","clipboard-encoding":"","dest-port":"","recording-exclude-output":"","recording-exclude-mouse":"","recording-include-keys":"","create-recording-path":"","enable-sftp":"","sftp-port":"","sftp-server-alive-interval":"","enable-audio":"","hostname":"@@{address}@@","security":"nla","disable-auth":"","ignore-cert":"true","gateway-port":"","server-layout":"","console":"","width":"","height":"","dpi":"","resize-method":"","console-audio":"","disable-audio":"","enable-audio-input":"","enable-printing":"","enable-drive":"","create-drive-path":"","enable-wallpaper":"","enable-theming":"","enable-font-smoothing":"","enable-full-window-drag":"","enable-desktop-composition":"","enable-menu-animations":"","disable-bitmap-caching":"","disable-offscreen-caching":"","disable-glyph-caching":"","preconnection-id":"","username":"@@{LOCAL.username}@@","password":"@@{LOCAL.secret}@@"},"attributes":{"max-connections":"","max-connections-per-user":"","weight":"","failover-only":"","guacd-port":"","guacd-encryption":""}}'


url     = "https://@@{Guacamole_IP}@@/api/session/data/mysql/connections?token=@@{calm_array_authToken}@@"
resp = urlreq(url, verb='POST', headers=headers,params=payload,send_form_encoded_data='FALSE')
if resp.ok:
  print "ConnectionIdentifier={0}".format(json.loads(resp.content)['identifier'])

else:
  print "Add Connection failed", json.dumps(json.loads(resp.content), indent=4)
  exit(1)