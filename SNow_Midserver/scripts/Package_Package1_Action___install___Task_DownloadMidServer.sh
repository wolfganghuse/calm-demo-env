echo "from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import os

options = Options()
options.headless = True

profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.panel.shown', False)
profile.set_preference('browser.download.folderList', 2)
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.dir', os.getcwd())
profile.set_preference('browser.helperApps.neverAsk.openFile', 'application/zip')
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/x-gzip')

browser = webdriver.Firefox(options=options,firefox_profile=profile)

browser.get('https://@@{Snow_Instance}@@/mid_server_download_ui.do')
time.sleep(20)
print('Sleep over')
browser.switch_to.frame('gsft_main')
print('entering creds')
username = browser.find_element_by_id('user_name')
password = browser.find_element_by_id('user_password')
username.send_keys('admin')
password.send_keys('@@{AdminPassword}@@')
login_attempt = browser.find_element_by_id('sysverb_login')
login_attempt.click()
print('Password entered')

time.sleep(30)
browser.switch_to.default_content()
browser.switch_to.frame('gsft_main')
downLink = browser.find_element_by_id('linux64')
print('DownLink Found')
downLink.click()
time.sleep(5)" > /tmp/DownloadMid.py
python3 /tmp/DownloadMid.py

sleep 5

while [ true ];do if [ ! -f mid*.part ];then break;fi;done 

chmod 777 mid*
mkdir -p nucalmmidser1
mv mid* nucalmmidser1/
cd nucalmmidser1
unzip mid*
rm -f mid*.*
cd agent
sed -i 's/YOUR_INSTANCE.service-now.com/@@{Snow_Instance}@@/g' config.xml
sed -i 's/YOUR_INSTANCE_USER_NAME_HERE/nucalmuser/g' config.xml
sed -i 's/YOUR_INSTANCE_PASSWORD_HERE/@@{AdminPassword}@@/g' config.xml
sed -i 's/YOUR_MIDSERVER_NAME_GOES_HERE/nucalmmidser1/g' config.xml

sh start.sh
sleep 30

echo "Service started"

echo "from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import os

options = Options()
options.headless = True

profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.panel.shown', False)
profile.set_preference('browser.download.folderList', 2)
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.dir', os.getcwd())
profile.set_preference('browser.helperApps.neverAsk.openFile', 'application/zip')
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/x-gzip')

browser = webdriver.Firefox(options=options,firefox_profile=profile)

browser.get('https://@@{Snow_Instance}@@/nav_to.do?uri=%2Fecc_agent.do%3Fsysparm_query=nameLIKEnucalmmidser1')
time.sleep(20)
print('Sleep over')
browser.switch_to.frame('gsft_main')
print('entering creds')
username = browser.find_element_by_id('user_name')
password = browser.find_element_by_id('user_password')
username.send_keys('admin')
password.send_keys('/@@{AdminPassword}@@')
login_attempt = browser.find_element_by_id('sysverb_login')
login_attempt.click()
print('Password entered')

time.sleep(20)

browser.switch_to.default_content()
browser.switch_to.frame('gsft_main')
browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
Validate_btn = browser.find_element_by_xpath('''//a[text()='Validate']''')
Validate_btn.click()
print('Validate Clicked')
time.sleep(10)
browser.quit()" > /tmp/ValidateMid.py
#python3 /tmp/ValidateMid.py
