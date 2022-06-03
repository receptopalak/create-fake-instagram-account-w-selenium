from calendar import month
import pdb
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os
import re
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from sqlalchemy import null
from undetected_chromedriver import Chrome
from bs4 import BeautifulSoup
from selenium.webdriver.common.proxy import Proxy, ProxyType

chromedriver="/usr/bin/chromedriver"
options = Options()
options.headless=True
prox = Proxy()
prox.proxy_type = ProxyType.MANUAL
prox.http_proxy = "68.183.97.200:80"
#prox.socks_proxy = "ip_addr:port"
prox.ssl_proxy = "188.166.124.18:80"

capabilities = webdriver.DesiredCapabilities.CHROME

def get_mail_id():
	prox.add_to_capabilities(capabilities)
	driver = Chrome(desired_capabilities=capabilities
	# ,options=options
	)
	# path = chromedriver
	# driver = webdriver.Chrome(executable_path = path)
	driver.get('https://www.minuteinbox.com/')
	driver.implicitly_wait(10)
	output = driver.page_source

	soup = BeautifulSoup(output, 'lxml')
	result = soup.findAll("span",{"id": "email"})

	for item in result:
		print(item)
		item = str(item)
		item = item.replace('</span>','')
		item = item.replace('<span class="animace" id="email" style="font-size: 1.4em;">','')

	return (item,driver)

def main():

	prox.add_to_capabilities(capabilities)
	driver = Chrome(desired_capabilities=capabilities,
	# options=options
	)
	# path = chromedriver
	# driver = webdriver.Chrome(executable_path = path)
	driver.get('https://www.instagram.com/accounts/emailsignup/?hl=en')
	driver.implicitly_wait(10)


# 	print(pyautogui.position())



# 	time.sleep(10)

# 	print(pyautogui.position())

# 	email = dom.find_element_by_name('emailOrPhone')
# 	fullname = dom.find_element_by_name('fullName')
# 	username = dom.find_element_by_name('username')
# 	password = dom.find_element_by_name('password')

	email = driver.find_element_by_css_selector("input[name='emailOrPhone']")
	fullname = driver.find_element_by_css_selector("input[name='fullName']")
	username = driver.find_element_by_css_selector("input[name='username']")
	password = driver.find_element_by_css_selector("input[name='password']")
	login_button = driver.find_element_by_xpath("//button[@type='submit']")
	
	# os.system('python3 mail_signup.py')
	
	(line, mail_driver) = get_mail_id()
	
	# f = open('temp.txt','r')
	# line = f.readline()

	email_enter = line
	full_name = email_enter.split('.')[0] + ' ' +email_enter.split('.')[1].split('@')[0]
	username_enter = full_name.replace(' ','')+'Jc12345ooottttssss'

	pyautogui.moveTo(400, 50)
	pyautogui.dragRel(800, 0,duration=1,button='left')

	
	email.send_keys(email_enter)
	fullname.send_keys(full_name)
	username.send_keys(username_enter)
	password.send_keys('xxxyyy')
	print('mail')
	print(email_enter)
	print('full name')
	print(full_name)
	print('username')
	print(username_enter)	
	print('password')
	print(password)
	login_button.click()
	time.sleep(10)
	
	select_month =driver.find_element_by_xpath("//select[@title='Month:']/option[text()='February']").click()
	select_dat =driver.find_element_by_xpath("//select[@title='Day:']/option[text()='1']").click()
	select_year =driver.find_element_by_xpath("//select[@title='Year:']/option[text()='1997']").click()
	next_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[6]/button')

	next_button.click()
	time.sleep(10)
	

	pyautogui.click(545, 423)
	time.sleep(2)
	pyautogui.click(545, 423)
	time.sleep(2)
	pyautogui.click(545, 423)
	time.sleep(2)
	pyautogui.click(625, 423)
	time.sleep(2)
	#pyautogui.click(626, 315)
	pyautogui.click(625, 423)
	time.sleep(2)
	pyautogui.click(705, 423)
	time.sleep(2)
	pyautogui.click(705, 800)
	time.sleep(2)
	pyautogui.click(626, 530)
	time.sleep(120)
	print('Getting page source')
	out = mail_driver.page_source
	soup = BeautifulSoup(out, 'lxml')
	result = soup.findAll("tbody",{"id": "schranka"})
	print(result)

	x=None
	for item in result:
		print('In For loop')
		print(item)
		item = str(item)
		x = re.findall("...... is your Instagram code", item)
		print(x)
		x = x[0]
		x = x[:6]
		break
	print(x)
	time.sleep(20)

	confirm = driver.find_element_by_css_selector("input[name='email_confirmation_code']")
	time.sleep(5)
	confirm.send_keys(x)
	time.sleep(5)
	confirm_button=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div/div[2]/button')
	time.sleep(5)
	confirm_button.click()
	time.sleep(10)

	

if __name__=="__main__":
    main()
