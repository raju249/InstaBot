from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from data import INSTA_LOGIN_URL
from data import USERNAME_AND_PASSWORD_DICT
from data import PATH_TO_CHROME_DRIVER

# Start Chrome Browser
driver = webdriver.Chrome(PATH_TO_CHROME_DRIVER)

# Load INstagram login Page
def load_page():
	return driver.get(INSTA_LOGIN_URL)

# Find login form on login page
def find_login_form():
	return driver.find_element_by_class_name("_rwf8p")

# Find username on login form
def find_username_field(login_form):
	return login_form.find_element_by_name("username")

# Find password on login form
def find_password_field(login_form):
	return login_form.find_element_by_name("password")

# Find and click login button on login form
def click_login_button(login_form):
	login_form.find_element_by_class_name("_aj7mu").click()
	return True

# Login user
def login_user(username,password):
	login_page = load_page()
	login_form = find_login_form()
	find_username_field(login_form).send_keys(username)
	find_password_field(login_form).send_keys(password)
	click_login_button(login_form)

def find_search_input():
	return driver.find_element_by_class_name('_9x5sw')

def find_click_follow_button():
	follow = driver.find_element_by_class_name('_aj7mu')
	follow.click()

def sleep():
	time.sleep(2)

def search_user(username):
	username_input = find_search_input()
	username_input.send_keys(username)
	sleep()
	username_input.send_keys(Keys.RETURN)

def load_user_profile_and_logout():
	driver.find_element_by_link_text('Profile').click()
	sleep()
	driver.find_element_by_class_name('_fcwm8').click()
	driver.find_element_by_class_name("_4y3e3").click()

# Main function a.k.a entry point of this bot
def main(username):
	for username in USERNAME_AND_PASSWORD_DICT.keys():
		login_user(username,USERNAME_AND_PASSWORD_DICT[username])
		print "Logged in as " + username
		sleep()
		search_user()
		sleep()
		find_click_follow_button()
		sleep()
		load_user_profile_and_logout()
		sleep()

	print "Done"

if __name__ == "__main__":
	print "Enter username: "
	main()





