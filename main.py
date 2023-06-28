from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_page_html(url):
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(url=url)
    sleep(3)

    # закрываем всплывающее окно
    modal_xpath = '//*[@id="__layout"]/div/div/div[7]/div[2]/div[2]/button[1]'
    WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, modal_xpath)))
    browser.find_element(By.XPATH, modal_xpath).click()

    # подтверждаем выбор города Москва
    moscow_xpath = '//*[@id="__layout"]/div/div/div[7]/div[2]/div[2]/button[1]'
    WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, moscow_xpath)))
    browser.find_element(By.XPATH, modal_xpath).click()

    # для выбора Санкт-Петербурга
    # choice_city_xpath = '//*[@id="__layout"]/div/div/div[7]/div[2]/div[2]/button[2]'
    # saint_petersburg_xpath = '//*[@id="__layout"]/div/div/div[7]/div[2]/div[2]/div/span[2]'

    # Кнопка "показать еще", нажимаем пока находим ее на странице
    more_xpath = '//*[@id="catalog-wrapper"]/main/div[2]/button'
    while True:
        try:
            if browser.find_element(By.XPATH, more_xpath):
                browser.find_element(By.XPATH, more_xpath).click()
                sleep(2)
        except:
            with open('result_pars_2.html', 'w') as file:
                file.write(browser.page_source)
            break

    browser.close()


def main():
    get_page_html('https://online.metro-cc.ru/category/bytovaya-himiya/chistyaschie-sredstva?in_stock=1&order=price_asc')


if __name__ == "__main__":
    main()
