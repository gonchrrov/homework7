import os.path
import time

import requests
from selene import query
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from script_os import TMP_DIR


def test_text_in_file():
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": TMP_DIR,
        "download.prompt_for_download": False,
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.config.driver = driver

    browser.open('https://github.com/pytest-dev/pytest/blob/main/README.rst')
    s("[data-testid='download-raw-button']").click()
    time.sleep(5)

    download_atr = s("[data-testid='raw-button']").get(query.attribute('href'))
    content = requests.get(url=download_atr).content
    with open(os.path.join(TMP_DIR, "readme2.rst"), "wb") as f:
        f.write(content)

    with open("tmp/readme2xx.rst") as f:
        file_content_str = f.read()
        assert 'test_answer' in file_content_str
