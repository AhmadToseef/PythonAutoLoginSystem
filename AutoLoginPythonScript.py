# importing liberaries
from selenium import webdriver
from getpass import getpass

# getting input from user
username = input("Enter Username: ")
password = getpass("Enter your password: ")

# getting reference of webDriver to access fields of web
driver = webdriver.Chrome("C:\\dev\\chromedriver\\chromedriver.exe")

# geting the url of the webpage which we want to access using this script
# in our case our site a hosted on localhost
driver.get("http://localhost:8080/phploginsystem/login.php")

# # accessing the field of this website to login
username_textBox = driver.find_element_by_name("username")
# # sending username to username field
username_textBox.send_keys(username)

password_textBox = driver.find_element_by_name("password")
password_textBox.send_keys(password)

login_button = driver.find_element_by_id("login")
login_button.submit()
