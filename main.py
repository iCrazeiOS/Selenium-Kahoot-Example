from selenium import webdriver
from time import sleep

pin = input("Enter Game Pin: ")
name = input("Enter Bot Name: ")

driver = webdriver.Chrome("./chromedriver")
driver.get("https://kahoot.it/")
print("\nLoading kahoot...\n")
sleep(2)

print("Entering Pin...")
driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/form/input")\
    .send_keys(pin)
print("Submitting Pin...\n")
driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/form/button")\
    .click()
sleep(4)

print("Entering Name...")
driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/form/input")\
    .send_keys(name)
print("Joining...")
driver.find_element_by_xpath("/html/body/div/div/div[1]/div/main/div/form/button")\
    .click()

print("In The Game!\n")

input("Press Enter Once The Answers Are Able To Be Clicked: ")

print("Selecting First Answer...")
driver.find_element_by_xpath("/html/body/div/div/main/div[2]/div/button[1]")\
	.click()
print("Selected First Answer")