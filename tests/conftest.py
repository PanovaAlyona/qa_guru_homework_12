import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser
from utils import attach


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()

selenoid_login = os.getenv("SELENOID_LOGIN")
selenoid_pass = os.getenv("SELENOID_PASS")
selenoid_url = os.getenv("SELENOID_URL")

@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    # Настройка capabilities для Selenoid
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "127.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    # Создаем драйвер для Selenoid
    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options
    )

    # Настройка Selene с созданным драйвером
    browser.config.driver = driver
    browser.config.timeout = 10
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser

    # Прикрепление артефактов
    attach.add_screenshot(browser.driver)
    attach.add_logs(browser.driver)
    attach.add_html(browser.driver)
    attach.add_video(browser.driver)

    browser.quit()