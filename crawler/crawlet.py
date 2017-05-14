#coding:utf-8
from crawler_single import Crawler_single
from db_management import dbManagement
import time
import random
import sys
import datetime
reload(sys)
sys.setdefaultencoding('utf-8')

class CrawlerMain:
    def __init__(self):
        self.choose_list = set()
        self.crawler_list = set()

    def begin_crawler(self, url):
        self.choose_list.add(url)
        self.main_crawler()

    def main_crawler(self):
        while self.choose_list:
            print '-' * 50
            choose_url = self.choose_list.pop()
            print str(datetime.datetime.now())
            print choose_url
            print "Total of chooseed list:  %s" % len(self.choose_list)
            print "Total of crawlered list: %s" % len(self.crawler_list)
            db = dbManagement()
            related_lists = []
            if db.has_id(choose_url.split('/')[-1]) is None:
                time.sleep(random.randint(2, 5))
                movie_obj = Crawler_single(choose_url)
                if not movie_obj.is_empty():
                    related_lists = movie_obj.getRecomment()
                    movie_id = movie_obj.getMovieId()
                    movie_name = movie_obj.getMovieName()
                    keywords = movie_obj.getKeyword()
                    rating_num = movie_obj.getRatingNum()
                    director = movie_obj.getDirector()
                    actor = movie_obj.getActor()
                    movie_type = movie_obj.getMovieType()
                    movie_date = movie_obj.getMovieDate()
                    runtime = movie_obj.getRunTime()
                    summary = movie_obj.getSummary()
                    db.insert_data(movie_id, movie_name, keywords, rating_num, director, actor, movie_type, movie_date, runtime, summary)
                    print "[%s][%s]" % (movie_id, movie_name)
            self.crawler_list.add(choose_url)
            self.update_chooselist(related_lists)


    def update_chooselist(self, related_list):
        for movie in related_list:
            if len(self.choose_list) < 100 and movie not in self.crawler_list:
                self.choose_list.add(movie)

if __name__ == '__main__':
#    initial_url = "https://movie.douban.com/subject/26593587"
    initial_url = "https://movie.douban.com/subject/26808466"
    CrawlerMain().begin_crawler(initial_url)
