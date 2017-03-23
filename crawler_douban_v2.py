#coding:utf-8
from bs4 import BeautifulSoup
from urllib2 import urlopen
from urllib2 import HTTPError
import traceback
import time
import random
import datetime
import pymysql


# 获取网页信息
class Crawler:
    def __init__(self, url):
        self.ds_obj = self.getContent(url)

    @staticmethod
    def getContent(url):
        try:
            html = urlopen(url)
            # print 'CODE:',html.getcode()
            bs_obj = BeautifulSoup(html, "html.parser")
        except HTTPError:
            traceback.print_exc()
            return None
        except AttributeError:
            traceback.print_exc()
            return None
        else:
            return bs_obj

    # 从h1中解析
    def getTitle(self):
        title = self.ds_obj.body.h1
        return title

    def getMovieName(self):
        title = self.getTitle()
        if (title):
            moviename = title.get_text().replace('\n', '')
        else:
            moviename = ''
        return moviename






if __name__ == '__main__':
    url = "https://movie.douban.com/subject/26630781"
    crawler = Crawler(url)
    title = crawler.getTitle()
    print title.find_all('span', attrs="year")
    print crawler.getMovieName()
