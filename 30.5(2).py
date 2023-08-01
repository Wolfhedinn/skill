import time
from selenium.webdriver.common.by import By
from main import driver
import pytest

def test_show_my_pets():
    #Open PetFriends base page:
    driver.get("http://petfriends.skillfactory.ru/login")

    #Вводим почту
    email_input = driver.find_element(By.ID, 'email')
    email_input.send_keys('@gmail.com')

    #Вводим пароль
    password_input = driver.find_element(By.ID, 'pass')
    password_input.send_keys('1234567890')

    #Нажимаем кнопку входа в аккаунт
    submith_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submith_button.click()

    #Проверка главной страницы
    images = driver.find_elements(By.CSS_SELECTOR, 'div:nth-of-tpe(2) > div > div > img')
    names = driver.find_elements(By.CSS_SELECTOR, 'div:nth-of-type(2) > h5')
    descriptions = driver.find_element(By.CSS_SELECTOR, 'div:nth-of-type(2) > p')

    for i in range(len(names)):
        assert images[i].get_attributes('src') != ''
        assert names[i].text !=''
        assert ', ' in descriptions[i].text
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0




