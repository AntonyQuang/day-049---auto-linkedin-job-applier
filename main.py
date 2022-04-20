from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from config import linkedin_username, linkedin_password, linkedin_mobile

# Setting up Selenium
chrome_driver_path = "C:\Development\chromedriver.exe"
s = Service(chrome_driver_path)

driver = webdriver.Chrome(service=s)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=marketing%20grad&location=London%2C%20England%2C%20United%20Kingdom")
driver.maximize_window()
sign_in = driver.find_element(by=By.CSS_SELECTOR, value=".nav__button-secondary")
sign_in.click()

username = driver.find_element(by=By.ID, value="username")
username.send_keys(linkedin_username)
password = driver.find_element(by=By.ID, value="password")
password.send_keys(linkedin_password)
sign_in_with_credentials = driver.find_element(by=By.CSS_SELECTOR, value=".from__button--floating")
sign_in_with_credentials.click()

time.sleep(5)

jobs = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-list__title")

for job in jobs:
    job.click()
    time.sleep(1)
    print(f"Applying for {job.text}")
    try:
        apply_job = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-apply-button")
        apply_job.click()

        time.sleep(1)

        mobile_input = driver.find_element(by=By.CSS_SELECTOR, value=".ember-view input")
        if mobile_input.text == "":
            mobile_input.send_keys(linkedin_mobile)

        next_button = driver.find_element(by=By.CSS_SELECTOR, value=".artdeco-button--primary")
        next_button.click()

        time.sleep(1)

        review_button = driver.find_element(by=By.CSS_SELECTOR, value=".artdeco-button--primary")
        if review_button.text == "Review":
            review_button.click()
            time.sleep(3)
            submit_button = driver.find_element(by=By.CSS_SELECTOR, value=".artdeco-button--primary")
            submit_button.click()
        else:
            dismiss_button = driver.find_element(by=By.CSS_SELECTOR, value=".artdeco-modal__dismiss")
            dismiss_button.click()
            time.sleep(0.5)
            discard_button = driver.find_element(by=By.CSS_SELECTOR, value=".artdeco-button--secondary")
            discard_button.click()
            print("Too complicated, skipped")
        time.sleep(2)
        try:
            dismiss_button = driver.find_element(by=By.CSS_SELECTOR, value=".artdeco-modal__dismiss")
            dismiss_button.click()
        except NoSuchElementException:
            time.sleep(2)
        continue
    except NoSuchElementException:
        print("Did this already, skipped")
        time.sleep(2)
    continue
    time.sleep(1)

time.sleep(5)
driver.quit()

