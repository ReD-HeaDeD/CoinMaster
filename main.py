import time
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By


class CoinParser(object):
    def __init__(self, driver):
        self.driver = driver

    def parse(self):
        self.driver.get("https://coinmarketcap.com/historical/")

        number_link = self.driver.find_elements(By.CLASS_NAME, 'historical-link')
        href_links = [number_link.get_attribute('href') for number_link in number_link[:]]
        with open("coin_list.txt", "w", encoding='utf-8') as file:
            for href_links_element in href_links[1:]:
                self.driver.get(href_links_element)
                time.sleep(1)
                pixal = 0

                while pixal <= 9000:
                    self.driver.execute_script(f'window.scrollTo(0, {pixal});')
                    pixal += 800
                    time.sleep(1)

                data = self.driver.find_element(By.XPATH, '//h1[contains(text(),"Historical Snapshot")]')
                coin = self.driver.find_elements(By.CLASS_NAME, 'cmc-table__column-name--name')
                price = self.driver.find_elements(By.XPATH, '//div[contains(text(),"$")]')
                coin_elements = [coin_element.text for coin_element in coin[:]]
                price_elements = [price_element.text for price_element in price[:]]
                coin_index = 0
                price_index = 1

                while len(coin_elements[:]) > coin_index:
                    file.write(f'{data.text}:{coin_elements[coin_index]}:{price_elements[price_index]}' + '\n')
                    coin_index += 1
                    price_index += 2


def main():
    driver = webdriver.Chrome()
    parser = CoinParser(driver)
    parser.parse()


if __name__ == '__main__':
    main()
