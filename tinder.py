import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

ops = Options()
ops.add_argument(
    "--user-data-dir=/Users/james-innes/Library/Application Support/Google/Chrome/")
ops.add_argument(r"--profile-directory=Profile 9")

d = webdriver.Chrome(options=ops)
d.get('https://tinder.com/app/recs')
time.sleep(5)

while True:
    time.sleep(1)
    ActionChains(d).send_keys(Keys.RIGHT).perform()
    ActionChains(d).send_keys(Keys.ESCAPE).perform()
    
