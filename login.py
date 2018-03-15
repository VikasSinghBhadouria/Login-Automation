from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import webbrowser
import time

usernameStr = 'ur gmail id'
passwordStr = 'ur gmail password'

browser = webdriver.Chrome()


browser.get(('https://accounts.google.com/ServiceLogin?'
             'service=mail&continue=https://mail.google'
             '.com/mail/#identifier'))

# fill in username and hit the next button

username = browser.find_element_by_id('identifierId')
username.send_keys(usernameStr)

nextButton = browser.find_element_by_id('identifierNext')
nextButton.click()

# wait for transition then continue to fill items

password = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.NAME, "password")))

password.send_keys(passwordStr)
time.sleep(3)

signInButton = browser.find_element_by_id('passwordNext')
signInButton.click()

# Wait for 10 seconds
time.sleep(10)

#second tab
browser.execute_script("window.open('about:blank', 'tab2');")
browser.switch_to.window("tab2")
browser.get('https://analytics.google.com/analytics/web/')


#third tab
browser.execute_script("window.open('about:blank', 'tab3');")
browser.switch_to.window("tab3")
browser.get('any other link')
