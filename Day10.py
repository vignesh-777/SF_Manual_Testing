import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://vinothqaacademy.com/demo-site/")

time.sleep(3)

first_name = driver.find_element(
    By.XPATH,
    "//label[contains(text(),'First Name')]/following::input[1]"
)

time.sleep(3)

first_name.send_keys("Vignesh")

time.sleep(3)

last_name = driver.find_element(
    By.XPATH,
    "//label[contains(text(),'Last Name')]/following::input[1]"
)

time.sleep(3)

last_name.send_keys("R")

time.sleep(3)

male = driver.find_element(
    By.XPATH,
    "//label[contains(.,'Male')]//input | //input[@value='Male']"
)

if not male.is_selected():
    male.click()

time.sleep(3)

selenium_webdriver = driver.find_element(
    By.XPATH,
    "//label[contains(.,'Selenium WebDriver')]//input | //input[@value='Selenium WebDriver']"
)

if not selenium_webdriver.is_selected():
    selenium_webdriver.click()

time.sleep(3)

java = driver.find_element(
    By.XPATH,
    "//label[contains(.,'Java')]//input | //input[@value='Java']"
)

if not java.is_selected():
    java.click()

time.sleep(3)

testng = driver.find_element(
    By.XPATH,
    "//label[contains(.,'TestNG')]//input | //input[@value='TestNG']"
)

if not testng.is_selected():
    testng.click()

time.sleep(3)

street_address = driver.find_element(
    By.XPATH,
    "//label[contains(text(),'Street Address')]/preceding::input[1]"
)

street_address.send_keys("123 Main Street")

time.sleep(3)

apt = driver.find_element(
    By.XPATH,
    "//label[contains(text(),'Apt, Suite, Bldg.')]/preceding::input[1]"
)

apt.send_keys("Apt 204")

time.sleep(3)

city = driver.find_element(
    By.XPATH,
    "//label[contains(text(),'City')]/preceding::input[1]"
)

city.send_keys("Chennai")

time.sleep(3)

state = driver.find_element(
    By.XPATH,
    "//label[contains(text(),'State / Province / Region')]/preceding::input[1]"
)

state.send_keys("Tamil Nadu")

time.sleep(3)

postal_code = driver.find_element(
    By.XPATH,
    "//label[contains(text(),'Postal / Zip Code')]/preceding::input[1]"
)

postal_code.send_keys("600001")

time.sleep(3)

country = Select(
    driver.find_element(
        By.XPATH,
        "//label[contains(text(),'Country')]/preceding::select[1]"
    )
)

country.select_by_visible_text("India")

time.sleep(3)

email = driver.find_element(
    By.XPATH,
    "//label[contains(text(),'Email')]/following::input[1]"
)

email.send_keys("vignesh@example.com")

time.sleep(3)

date_demo = driver.find_element(
    By.XPATH,
    "//label[contains(text(),'Date of Demo')]/following::input[1]"
)

date_demo.send_keys("10/15/26")

time.sleep(3)

print("First Name:", first_name.get_attribute("value"))
print("Last Name:", last_name.get_attribute("value"))
print("Street Address:", street_address.get_attribute("value"))
print("Apt:", apt.get_attribute("value"))
print("City:", city.get_attribute("value"))
print("State:", state.get_attribute("value"))
print("Postal Code:", postal_code.get_attribute("value"))
print("Country:", country.first_selected_option.text)
print("Email:", email.get_attribute("value"))
print("Date:", date_demo.get_attribute("value"))

print("Form fields completed successfully!")

input("Press ENTER to close browser...")

driver.quit()