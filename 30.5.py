from selenium.webdriver.common.by import By
from toolz import partition
import pytest

from selenium.webdriver.support.ui import WebdriverWait
from selenium.webdriver.support import expected_conditions as ec
from conftest import my_email, my_password, my_nickname
import re

@pytest.fixture(autouse-True)
def testing(web_browser):
    web_browser.get("http://petfriends.skillfactory.ru/login")
    # Водим email
    field_email - web_browser.find_element(By.ID,"email")
    field_email.clear()
    field_email.send_keys(my_email)

    # addpassword
    field_pass = web_browser.find_element(By.ID,"pass")
    field_pass.clear()
    field_pass.send_keys(my_passwor)

    # click submith button
    btn_submit = web_browser.find_element(By.XPATH,"//button[@type='submit']")
    btn_submit.click()
    assert  web_browser.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    btn_MyPets = web_browser.find_element(By.CSS_SELECTOR, "div#navbarNav > ul > li > a")
    btn_MyPets.click()
    assert  web_browser.find_element(By.CSS_SELECTOR, "html = body > div > div > h2").text == my_nickname