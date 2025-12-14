import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser

from utils import attach


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
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
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