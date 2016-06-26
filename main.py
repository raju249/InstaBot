from selenium import webdriver
import time
import sys
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

# Find search input box
def find_search_input():
	return driver.find_element_by_class_name('_9x5sw')

# Find and click follow button
def find_click_follow_button():
	follow = driver.find_element_by_class_name('_aj7mu')
	follow.click()

# Sleep for 2 seconds
def sleep():
	time.sleep(2)

# Search given username
def search_user(username):
	username_input = find_search_input()
	username_input.send_keys(username)
	sleep()
	username_input.send_keys(Keys.RETURN)

# Load user Profile to logout
def load_user_profile_and_logout():
	driver.find_element_by_link_text('Profile').click()
	sleep()
	driver.find_element_by_class_name('_fcwm8').click()
	driver.find_element_by_class_name("_4y3e3").click()

# Main function a.k.a entry point of this bot
def main(username):
	for user in USERNAME_AND_PASSWORD_DICT.keys():
		login_user(user,USERNAME_AND_PASSWORD_DICT[user])
		print "Logged in as " + user
		sleep()
		search_user(username)
		sleep()
		find_click_follow_button()
		sleep()
		load_user_profile_and_logout()
		sleep()

	print "Added followers to " + username

# Run at start
if __name__ == "__main__":
	while True:
		user = raw_input("Enter username (q to quit): ")
		if user.startswith("q"):
			sys.exit(0)
		main(user)