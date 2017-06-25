# coding:utf-8
from selenium import webdriver

EXECUTE_PATH = r"D:\phantomjs\bin\phantomjs"

class CrawlerOWNet:
    def __init__(self, url):
        self.url = url
        self.net_driver = self.__get_driver()

    def __del__(self):
        self.net_driver.close()

    def __get_driver(self):
        driver = webdriver.PhantomJS(executable_path=EXECUTE_PATH)
        driver.get(self.url)
        return driver

    def get_basic_element(self):
        basic_info = []
        for i in range(1, 15):
            value = self.net_driver.find_element_by_id("gt%s" % str(i)).text
            basic_info.append(value)
        return basic_info

    def get_id(self):
        return self.net_driver.find_element_by_id("name").text

    def get_code(self):
        return self.net_driver.find_element_by_id("code").text

if __name__ == "__main__":
    # crawler_obj = CrawlerOWNet("http://quote.eastmoney.com/sh600519.html")
    crawler_obj = CrawlerOWNet("http://quote.eastmoney.com/zs000010.html")
    print crawler_obj.net_driver.page_source
    #print crawler_obj.get_basic_element()
    #print crawler_obj.get_id()
    #print crawler_obj.get_code()
