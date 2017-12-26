from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import getpass


def openFB():
	global browser
	try:
		browser = webdriver.Chrome('/media/akshat/Others/Programs/Selenium Webdrivers/chromedriver')
	except:
		print("Couldn't open Chrome browser. Make you have Chrome installed and the path of the chromedriver is correct.")
	browser.get('https://www.facebook.com/')
	return


def login(fb_ID, password):
	user = browser.find_elements_by_xpath('//*[@id="email"]')
	user[0].send_keys(fb_ID)
	user = browser.find_elements_by_xpath('//*[@id="pass"]')
	user[0].send_keys(password)
	LOG = browser.find_elements_by_xpath('//*[@id="loginbutton"]')
	LOG[0].click()
	#print("Login Successfull")
	return


def wish():
	browser.get('https://www.facebook.com/events/birthdays/')
	wish = browser.find_elements_by_xpath('//*[@class="enter_submit uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea inlineReplyTextArea mentionsTextarea textInput"]')
	if len(wish)==0:
		print("Either login failure or no birthdays today")
		return
	count = 0;
	print("Wishing...")
	for friend in wish:
		try:
			friend.send_keys('Happy birthday! :)')			#Customize the birthday wish
			friend.send_keys(Keys.RETURN)
			count += 1
		except:
			print("Either already wished or has disabled posts on timeline.")
			#continue
		time.sleep(2)
	if(count==0):
		print("None of your friends have their birthday today!")
	elif(count==1):
		print("1 person was wished successfully!")
	else:
		print(str(count) + " people were wished successfully!")
	return



openFB()
fb_ID = raw_input("Enter facebook ID: ")
password = getpass.getpass("Password: ")
print('Logging in facebook...')
login(fb_ID, password)
wish()


browser.close()


