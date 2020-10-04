from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())



PROXY = " "
PROXY = input("PLEASE ENTER Proxy IP & wait (Step 2):      ")
webdriver.DesiredCapabilities.CHROME['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "noProxy": None,
    "proxyType": "MANUAL",
    "autodetect": False
}




user_agent = " "
user_agent = input("PLEASE ENTER User Agent & wait:      ")
opts = Options()
opts.add_argument("user-agent=" + user_agent)
driver = webdriver.Chrome(ChromeDriverManager().install(),options=opts)
# driver = webdriver.Chrome(options=opts)
String_userAgent = driver.execute_script("return navigator.userAgent")
print(String_userAgent)



#cut paste from ip proxy code
print(PROXY)
time.sleep(20)
driver.get('https://www.whatsmyip.org/')
time.sleep(20)
print(PROXY)
