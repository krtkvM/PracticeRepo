import unittest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

# browser.implicitly_wait(5)

class Tests(unittest.TestCase):

    def setUp(self):
        # link1 = "http://suninjuly.github.io/registration1.html"
        # link2 = "http://suninjuly.github.io/registration2.html"
        self.browser = webdriver.Chrome()

    def test_reg1(self):
        link1 = "http://suninjuly.github.io/registration1.html"
        browser = self.browser #webdriver.Chrome()
        browser.get(link1)
        self.input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        self.input1.send_keys("Ivan1")
        self.input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        self.input2.send_keys("Petrov")
        self.input3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        self.input3.send_keys("Smolensk@sm.sm")
        self.button = browser.find_element_by_css_selector("button.btn")
        self.button.click()
        self.welcome_text_elt = browser.find_element_by_tag_name("h1")
        self.welcome_text = self.welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", self.welcome_text, "FAILED. You are die")
        # assert "Congratulations! You have successfully registered!" == self.welcome_text

    def test_reg2(self):
        link2 = "http://suninjuly.github.io/registration2.html"#cf
        browser = self.browser# webdriver.Chrome()
        browser.get(link2)
        self.input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        self.input1.send_keys("Ivan1")
        self.input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        self.input2.send_keys("Petrov")
        self.input3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        self.input3.send_keys("Smolensk@sm.sm")
        self.button = browser.find_element_by_css_selector("button.btn")
        self.button.click()
        self.welcome_text_elt = browser.find_element_by_tag_name("h1")
        self.welcome_text = self.welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", self.welcome_text, "FAILED. You are die")

        # assert "Congratulations! You have successfully registered!" == self.welcome_text
if __name__ == "__main__":
    unittest.main()
# try:
#     link = "http://suninjuly.github.io/registration1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # Ваш код, который заполняет обязательные поля
#     input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
#     input1.send_keys("Ivan1")
#     input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
#     input3.send_keys("Smolensk@sm.sm")
#
#     # Отправляем заполненную форму
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(1)
#
#     # находим элемент, содержащий текст
#     welcome_text_elt = browser.find_element_by_tag_name("h1")
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text
#
#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()