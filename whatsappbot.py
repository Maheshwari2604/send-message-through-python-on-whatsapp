from selenium import webdriver

#import os
#driver = os.system("firefox  --new-tab https://web.whatsapp.com/")


driver = webdriver.Chrome()
driver.get('http://web.whatsapp.com')

name = raw_input('Enter the name of user or group : ')
print name
msg = raw_input('Enter the message : ')
count = int(raw_input('Enter the count : '))

#Scan the code before proceeding further
#input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))

#user = driver.find_element_by_xpath("//span[@title = 'Papa']").text
print user

user.click()

msg_box = driver.find_element_by_class_name('_2S1VP copyable-text selectable-text')

for i in range(count):
    msg_box.send_keys(msg)
driver.find_element_by_class_name('_35EW6').click()
