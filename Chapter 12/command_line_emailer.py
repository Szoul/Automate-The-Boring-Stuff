#! python 3.8
# command_line_emailer.py: log into mail account and send a mail with text (provided as command) to another email (also provided via command) via selenium
# finished project on Sept/2020 (might stop working if html changes)

# take command input
# log into mail account
# create a new mail and fill in adress and text
# send mail
# log out

import sys, selenium, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

adress = sys.argv[1]            # who needs input validation anyway?
text = sys.argv[2]

my_email_adress = input("Enter your mail adress")
my_password = input("Enter your Password")
link_to_mail_login = "https://web.de"
mail_adress_to_sent_to = str(adress)
text_to_send = str(text)

#open browser to login-URL
browser = webdriver.Firefox()
browser.get(link_to_mail_login)
time.sleep(5)

#login
login_username = browser.find_element_by_id("freemailLoginUsername")
login_username.send_keys(f"{my_email_adress}")
login_password = browser.find_element_by_id("freemailLoginPassword")
login_password.send_keys(f"{my_password}")
login_button = browser.find_element_by_xpath('//*[@id="freemailLoginForm"]/button')
login_button.click()
time.sleep(5)

#open new mail
    # Problem: cant find element/ element is a button
    # Solution: has to do with iframes (https://stackoverflow.com/questions/57125553/selenium-cant-find-99-of-elements-why)
    # no idea what this excatly does yet: (wait and switch into iframe, then click element by xpath)
    # what is an iframe? - short for "Inline Frame" - used to embed another (html-) Document into the current HTML Doc
        # while webscraping, you have to enter the specific frame, then continue as usual
WebDriverWait(browser,20).until(EC.frame_to_be_available_and_switch_to_it((By.NAME,'home')))
WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH,'//div[@id="navigation"]//ul//li[@class="item"]//a[@title="E-Mail schreiben"]'))).click()
browser.switch_to.default_content()     # --> leave frame even though new site is already loaded


time.sleep(5)
browser.switch_to.frame(browser.find_element_by_xpath('//*[@id="thirdPartyFrame_mail"]'))
mail_to_input = browser.find_element_by_class_name('select2-input')
mail_to_input.send_keys(f"{mail_adress_to_sent_to}")

browser.switch_to.frame(browser.find_element_by_xpath('//*[@id="cke_1_contents"]/iframe'))
# text field is in a new iframe with no apparent <input> element
    # text that is entered there is saved as a <div> , one div for each line 
    # apparently "send_keys() to the body element works just fine"
browser.find_element_by_xpath('//*[@id="body"]').send_keys(f"{text_to_send}")
browser.switch_to.parent_frame()

#send ()
browser.find_element_by_xpath('//*[@id="compose-send-button"]').click()
browser.switch_to.default_content()

#logout
browser.find_element_by_xpath('/html/body/atlas-app/atl-navbar/atl-actions-menu/div[1]/div[2]/pos-icon-item[2]').click()