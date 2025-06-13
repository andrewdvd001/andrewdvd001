from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver (using Chrome in this example)
driver = webdriver.Chrome()  # Make sure you have chromedriver installed
driver.maximize_window()  # Maximize window for better screenshot visibility

try:
    # 1. Navigate to the contact page
    driver.get("https://javan.co.id/contactus")
    
    # Wait for form to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="oy3vgnjvlko"]'))
    )
    time.sleep(3)
    # 2. Fill out the form
    driver.find_element(By.XPATH, '//*[@id="oy3vgnjvlko"]').send_keys("Test User")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="oh690azrrbm8"]').send_keys("Tester")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="o584cozj4jan"]').send_keys("test@example.com")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="ozvo3ntfn2x"]').send_keys("Testing form submission without reCAPTCHA")
    time.sleep(3)
    
    # 3. Take screenshot before submission
    driver.save_screenshot("contact_form_before_submission.png")
    print("Screenshot taken before submission: contact_form_before_submission.png")
    
    # 4. Submit the form
    submit_button = driver.find_element(By.XPATH, '//*[@id="wrap"]/section/div/div/div[2]/section/div/form/div/div[10]/a')
    submit_button.click()
    
    # Wait a moment to see if any reCAPTCHA appears
    time.sleep(3)
    
    # 5. Take screenshot after submission
    driver.save_screenshot("contact_form_after_submission.png")
    print("Screenshot taken after submission: contact_form_after_submission.png")
    
    print("Bug reproduction and screenshot capture complete!")
    
finally:
    # Close the browser
    driver.quit()