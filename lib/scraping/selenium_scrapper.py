from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from platform import system
from sys import exit
from bs4 import BeautifulSoup

class SeleniumWebScraper:
    def __get_driver(self):
        sys = system()
        if sys == 'Windows':
            service = Service('./drivers/chromedriver_win64.exe')
        elif sys == 'Darwin':
            service = Service('./drivers/chromedriver_mac_arm')
        elif sys == 'Linux':
            service = Service('./drivers/chromedriver_linux64')
        else:
            print('Operating system not supported, try use bs4. Aborting...')
            exit()
        return service

    def __init__(self) -> None:
        self.__options = Options()
        self.__options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.__options, service=self.__get_driver())
        self.__department_section = {
            'container':{
            'xpath':'/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div[2]',
            'css-selector':'#CardInstancexoVVa3XiEH3QsYt-pxTbIA > div:nth-child(2) > div:nth-child(2)',
            'class-name':'_p13n-zg-nav-tree-all_style_zg-browse-group__88fbz'
            },
            'childs':{
                'xpath':'/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div',
                'css-selector':'#CardInstancexoVVa3XiEH3QsYt-pxTbIA > div:nth-child(2) > div:nth-child(2) > div',
                'class-name':'_p13n-zg-nav-tree-all_style_zg-browse-item__1rdKf _p13n-zg-nav-tree-all_style_zg-browse-height-large__1z5B8'
            }
        }

    def __find_element(self, props):
        try:
            return self.driver.find_element(By.XPATH, props['xpath'])
        except NoSuchElementException:
            try:
                return self.driver.find_element(By.CSS_SELECTOR, props['css-selector'])
            except NoSuchElementException:
                try:
                    return self.driver.find_element(By.CLASS_NAME, props['class-name'])
                except Exception as e:
                    print('Element not found: {0}'.format(e))
                    exit()

    def __find_elements(self, props, father=None):
        if father is not None:
            container = self.__find_element(father)
            try:
                return container.find_elements(By.XPATH, props['xpath'])
            except NoSuchElementException:
                try:
                    return container.find_elements(By.CSS_SELECTOR, props['css-selector'])
                except NoSuchElementException:
                    try:
                        return container.find_elements(By.CLASS_NAME, props['class-name'])
                    except Exception as e:
                        print('Element not found: {0}'.format(e))
                        exit()
        else:
            try:
                return self.driver.find_elements(By.XPATH, props['xpath'])
            except NoSuchElementException:
                try:
                    return self.driver.find_elements(By.CSS_SELECTOR, props['css-selector'])
                except NoSuchElementException:
                    try:
                        return self.driver.find_elements(By.CLASS_NAME, props['class-name'])
                    except Exception as e:
                        print('Element not found: {0}'.format(e))
                        exit()

    def parse_page(self, url):
        self.driver.get(url)
        elem = self.__find_elements(self.__department_section['childs'], self.__department_section['container'])
        for i in elem:
            print(i.text)
            # print(i.get_attribute('href'))

    def get_page(self, url):
        self.driver.get(url)
        return str(BeautifulSoup(self.driver.page_source, 'html.parser').prettify())
    
    def close(self):
        self.driver.close()

def parse_page(URL):
    sel = SeleniumWebScraper()
    sleep(2)
    res = sel.parse_page('https://www.amazon.com.br/gp/bestsellers/computers/')
    sel.close()
    return res

if __name__ == '__main__':
    parse_page('https://www.amazon.com.br/gp/bestsellers/computers/')