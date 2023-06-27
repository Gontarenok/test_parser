from time import sleep
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

browser.maximize_window()
browser.get('https://online.metro-cc.ru/category/bytovaya-himiya/chistyaschie-sredstva?in_stock=1&order=price_asc')
# WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".reply-button"))).click()

modal_xpath = '//*[@id="__layout"]/div/div/div[7]/div[2]/div[2]/button[1]'
WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, modal_xpath)))
browser.find_element(By.XPATH, modal_xpath).click()

moskow_xpath = '//*[@id="__layout"]/div/div/div[7]/div[2]/div[2]/button[1]'
WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, moskow_xpath)))
browser.find_element(By.XPATH, modal_xpath).click()


# count_xpath = '//*[@id="catalog-wrapper"]/main/div[2]/div[1]/span'
# WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, count_xpath)))
# count = browser.find_element(By.XPATH, count_xpath)
#
# count_int = re.sub(r'\D', '', count.text)
# print(f'Количество товаров в категории: {count_int}')

more_xpath = '//*[@id="catalog-wrapper"]/main/div[2]/button'

while True:
    try:
        if browser.find_element(By.XPATH, more_xpath):
            browser.find_element(By.XPATH, more_xpath).click()
            sleep(2)
    except:
        with open('result_pars.html', 'w') as file:
            file.write(browser.page_source)
        break





    # WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, more_xpath)))
    # browser.find_element(By.XPATH, more_xpath).click()



sleep(10)

browser.close()

choice_city_xpath = '//*[@id="__layout"]/div/div/div[7]/div[2]/div[2]/button[2]'
saint_peterburg_xpath = '//*[@id="__layout"]/div/div/div[7]/div[2]/div[2]/div/span[2]'