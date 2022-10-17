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

        #year = self.driver.find_elements(By.CLASS_NAME, 'lgiEcX')
        #month = self.driver.find_elements(By.CLASS_NAME, 'eSQiCH')
        #number = self.driver.find_elements(By.CLASS_NAME, 'historical-link')

        """year_elements = [year_element.text for year_element in year[:]]
        #print(f'[year]: {year_elements}')
        number_elements = [number_element.text for number_element in number[:]]
        #print(f'[number]: {number_elements}')
        index_year = 0
        index_number = 0
        extra_line = ''
        for month_element in month[:]:
            print(f'[year]: {year_elements[index_year]} - '
                  f'[month]: {month_element.text} - '
                  f'[number]: {number_elements[index_number] + extra_line}')
            index_number += 1
            extra_line = ''
            if month_element.text == 'December':
                index_year += 1
            while int(number_elements[index_number]) < 24:
                extra_line = extra_line + ', ' + number_elements[index_number]
                index_number += 1"""

        number_link = self.driver.find_elements(By.CLASS_NAME, 'historical-link')
        href_links = [number_link.get_attribute('href') for number_link in number_link[:]]
        with open("coin_list.txt", "w", encoding='utf-8') as file:
            for href_links_element in href_links[1:]:
                self.driver.get(href_links_element)
                time.sleep(1)
                data = self.driver.find_element(By.XPATH, '//h1[contains(text(),"Historical Snapshot")]')
                coin = self.driver.find_elements(By.CLASS_NAME, 'cmc-table__column-name--name')
                price = self.driver.find_elements(By.XPATH, '//div[contains(text(),"$")]')
                coin_elements = [coin_element.text for coin_element in coin[:]]
                price_elements = [price_element.text for price_element in price[:]]
                coin_index = 0
                price_index = 1

                while len(coin_elements[:]) > coin_index:
                        #print(f'data: {data.text},'f'coin: {coin_elements[coin_index]}, 'f'price: {price_elements[price_index]}')
                        file.write(f'{data.text}:{coin_elements[coin_index]}:{price_elements[price_index]}' + '\n')
                        coin_index += 1
                        price_index += 2

        """for number_elem_pandas in number[:]:
            crypto_coin = ({'number': [number_elem_pandas.text]})
            album_df = pd.DataFrame(crypto_coin)
            print(album_df)"""

        """for year_element, month_element, number_element in zip(year[:], month[:], number[:]):
            print(f'[year]: {year_element.text} [month]: {month_element.text} [month]: {number_element.text}')
            crypto_coin = ({'year': [year_element.text],
                           'month': [month_element.text],
                           'number': [number_element.text]})

            album_df = pd.DataFrame(crypto_coin)
            #print(album_df)"""


def main():
    driver = webdriver.Chrome()
    parser = CoinParser(driver)
    parser.parse()


if __name__ == '__main__':
    main()
