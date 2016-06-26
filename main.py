from selenium import webdriver
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

# Main function a.k.a entry point of this bot
def main():
	for username in USERNAME_AND_PASSWORD_DICT.keys():
		login_user(username,USERNAME_AND_PASSWORD_DICT[username])
		print "Logged in as " + username
	print "Done"

if __name__ == "__main__":
	main()





