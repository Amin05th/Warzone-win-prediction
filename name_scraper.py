import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, \
    ElementNotInteractableException


def fetch_names(path, num_page):
    text_list = []
    options = Options()
    options.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(executable_path=path, options=options)
    driver.get('https://cod.tracker.gg/warzone/leaderboards/battle-royale/psn/Wins?page=1')
    current_page = 1

    time.sleep(10)

    while current_page <= num_page:
        done = False
        while not done:
            try:
                time.sleep(5)
                text_fields = driver.find_elements(By.XPATH, ".//span[@class='trn-ign__username']")
                text_list.extend(i.text for i in text_fields)
            except NoSuchElementException:
                text_list.append("-1")
            done = True

        if done:
            print(f'{current_page} out of {str(num_page)} pages done')
            current_page += 1
            driver.get(f'https://cod.tracker.gg/warzone/leaderboards/battle-royale/psn/Wins?page={current_page}')

    return text_list
