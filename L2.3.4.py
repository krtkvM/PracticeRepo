import os

from selenium import webdriver
import time
import math

from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button_magic_journey = browser.find_element(By.XPATH, "//button[@type='submit']")
    button_magic_journey.click()

    confirm_modal = browser.switch_to.alert
    confirm_modal.accept()

    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = x_element.text
    y = calc(x)

    input_answer = browser.find_element(By.XPATH, "//input[@id='answer']")
    input_answer.send_keys(y)

    sbmtbutton = browser.find_element(By.XPATH, "//button[@type='submit']")
    sbmtbutton.click()

    alertmodal = browser.switch_to.alert
    alertmodaltext = alertmodal.text.split(': ')[-1]
    print(alertmodaltext)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
