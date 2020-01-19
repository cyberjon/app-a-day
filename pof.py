from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://www.pof.com/login.aspx")

username = browser.find_element_by_id("logincontrol_username")
password = browser.find_element_by_id("logincontrol_password")
submit   = browser.find_element_by_id("logincontrol_submitbutton")

username.send_keys("Code_Wizard_82")
password.send_keys("nx-596501pof.")

submit.click()


browser.get("https://www.pof.com/meetme.aspx#meetmetop")





while True:
    for i in range(1,10):
        meet_me_yes = browser.find_element_by_id("meet-me-button-yes-var")
        meet_me_yes.click()
        browser.refresh();
    
       
    # Break on even random number.
    if i == 9:
        break
    
    



