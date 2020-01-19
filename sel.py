
import sys
driver = webdriver.Chrome()

#driver.get(sys.argv[-1])
driver.get('https://www.instagram.com/p/B2ztH74BCKq/')

elems = driver.find_elements_by_xpath("//a[@class='FPmhX notranslate TlrDj']")

users = []

for elem in elems:
    users.append(elem.get_attribute('title'))
    print('Nmae Peopel who liked this post: ' +elem.get_attribute('title'))


driver.quit()
