from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
Android apps automation template

1. Install appium. `npm install -g appium`
2. Install android studio sdk.
3. appium python. `python3 -m pip install Appium-Python-Client`
4. set env `ANDROID_HOME=C:\\Users\username\AppData\Local\Android\Sdk`
5. Run `appium` on different terminal
6. `python3 test-appium.py`
"""

from time import sleep

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'Bla bla'
desired_caps['appPackage'] = 'jp.blabla'
desired_caps['appActivity'] = 'jp.blabla.MainActivity'
desired_caps["noReset"]  = "true"
desired_caps["fullReset"]  = "false"

# setup driver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# Tap on a button
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_all_elements_located((MobileBy.XPATH, "XPATH BUTTON")))

button = driver.find_element(MobileBy().XPATH, "XPATH BUTTON")
TouchAction(driver).tap(button).perform()

# Enter text
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_all_elements_located((MobileBy.XPATH, "XPATH FORM")))

text_field = driver.find_element(MobileBy().XPATH, "XPATH FORM")
text_field.send_keys('INPUT TEST')

# Get text
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_all_elements_located((MobileBy.XPATH, "XPATH TEXTBOX")))

text_field = driver.find_element(MobileBy().XPATH, "XPATH TEXTBOX")
text = text_field.text

print(text)

end = time.time()
print(end - start)

driver.quit()
