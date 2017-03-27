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
        self.bs_obj = self.__getContent(url)

    @staticmethod
    def __getContent(url):
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

    # 从title中解析电影名
    def getMovieName(self):
        title = self.bs_obj.body.h1
        if (title):
            moviename = title.get_text().replace('\n', '')
        else:
            moviename = ''
        return moviename

    # 解析关键字
    def getKeyword(self):
        keyword_module = self.bs_obj.find_all(attrs={"name": "keywords"})
        if keyword_module:
            keyword = keyword_module[0]["content"]
        else:
            keyword = ''
        return keyword

    # 读取豆瓣评分
    def getRatingNum(self):
        ratingnum_module = self.bs_obj.find_all(attrs={"class": "ll rating_num", "property": "v:average"})
        if ratingnum_module:
            rating_num = ratingnum_module[0].get_text()
        else:
            rating_num = ''
        return rating_num

    # 读取导演信息
    def getDirector(self):
        director_module = self.bs_obj.find_all(attrs={"rel": "v:directedBy"})
        if director_module:
            director = self.bs_obj.find_all(attrs={"rel": "v:directedBy"})[0].get_text()
        else:
            director = ''
        return director

    # 读取导演ID

    # 读取演员信息
    def getActor(self):
        actor_module = self.bs_obj.find_all(attrs={"class": "actor"})
        if actor_module:
            for actor in actor_module[0].find_all(attrs={"rel": "v:starring"}):
                print actor.get("href")
            actor = self.bs_obj.find_all(attrs={"class": "actor"})[0].get_text()
            # actor = self.bs_obj.find_all(attrs={"class": "actor"})[0].get_text().replace(' ', '').replace('/', ',').split(':')[1]
        else:
            actor = ''
        return actor

    # 读取演员ID

if __name__ == '__main__':
    url = "https://movie.douban.com/subject/26630781"
    crawler = Crawler(url)
    print crawler
    print "MovieName:", crawler.getMovieName()
    print "Keyword:", crawler.getKeyword()
    print "RatingNum:", crawler.getRatingNum()
    print "Director:", crawler.getDirector()
    print "Actors:", crawler.getActor()

