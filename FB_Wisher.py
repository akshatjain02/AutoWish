from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import getpass


def openFB():
	global browser
	browser = webdriver.Chrome('/media/akshat/Others/Programs/Selenium Webdrivers/chromedriver')
	browser.get('https://www.facebook.com/')
	return


def login(fb_ID, password):
	print('Logging in facebook...')
	user = browser.find_elements_by_xpath('//*[@id="email"]')
	user[0].send_keys(fb_ID)
	user = browser.find_elements_by_xpath('//*[@id="pass"]')
	user[0].send_keys(password)
	LOG = browser.find_elements_by_xpath('//*[@id="loginbutton"]')
	LOG[0].click()
	print("Login Successfull")
	return


def wish():
	browser.get('https://www.facebook.com/events/birthdays/')
	wish = browser.find_elements_by_xpath('//*[@id="u_0_z"]')
	count = 0;
	print("Wishing...")
	for friend in wish:
		friend.send_keys('Happy birthday! :)')			#Customize the birthday wish
		friend.send_keys(Keys.RETURN)
		time.sleep(2)
		count += 1
	if(count==0):
		print("None of your friends have their birthday today!")
	elif(count==1):
		print("1 person was wished successfully!")
	else:
		print(count + " people were wished successfully!")
	return



openFB()
fb_ID = raw_input("Enter facebook ID: ")
password = getpass.getpass("Password: ")
login(fb_ID, password)
wish()


browser.close()


