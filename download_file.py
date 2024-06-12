import time
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": "/Users/goncharov/QAGURU/homework7/tmp",
    "download.prompt_for_download": False,
}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
browser.config.driver = driver

browser.open('https://github.com/pytest-dev/pytest/blob/main/README.rst')
s("[data-testid='download-raw-button']").click()
time.sleep(5)
