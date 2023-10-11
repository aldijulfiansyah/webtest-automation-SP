from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
# Inisialisasi driver Chrome
driver = webdriver.Chrome()

# Buka halaman Selenium
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# mengambil title page
title = driver.title

#apakah title sama atau tidak jika sama lanjut
assert title =="Web form"

#menunggu apakah elemennt ada atau tidak selama 0.5dtk
driver.implicitly_wait(0.5)


text_box = driver.find_element(by=By.NAME, value="my-text")
text_area = driver.find_element(by=By.NAME, value="my-textarea")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
dropdown = driver.find_element(by=By.NAME, value="my-select")

#set element input
text_box.send_keys("Selenium")
text_area.send_keys("H")

#klik element select
select = Select(dropdown)

#memilih element select dengan text "One"
select.select_by_visible_text("One")

time.sleep(10) #mengunggu 10 detik untuk memastikan data terisi sebelum disubmit
submit_button.click()


message = driver.find_element(by=By.ID, value="message")
value = message.text
assert value == "Received!"

time.sleep(5)



# Tutup browser
driver.quit()