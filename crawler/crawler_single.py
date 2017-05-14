#coding:utf-8
from bs4 import BeautifulSoup
from urllib2 import urlopen
from urllib2 import HTTPError
from urllib2 import URLError
import traceback
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 获取网页信息,通过url解析网页
class Crawler_single:
    def __init__(self, url):
        self.bs_obj = self.__getContent(url)
        self.url = url

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
        except URLError:
            traceback.print_exc()
            return None
        else:
            return bs_obj

    def getMovieId(self):
        return self.url.split('/')[-1]

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
            rating_num = -1
        return rating_num

    # 读取导演信息
    def getDirector(self):
        director_module = self.bs_obj.find_all(attrs={"rel": "v:directedBy"})
        if director_module:
            director = director_module[0].get_text()
        else:
            director = ''
        return director

    # 读取导演ID
    def getDirectorId(self):
        director_module = self.bs_obj.find_all(attrs={"rel": "v:directedBy"})
        reobj = re.compile("[0-9]+")
        director_id = 0
        if director_module:
            m = re.search(reobj, director_module[0].get("href"))
            if m is not None:
                director_id = m.group(0)
        return director_id

    # 读取演员信息
    def getActor(self):
        actor_module = self.bs_obj.find_all(attrs={"class": "actor"})
        if actor_module:
            actor = actor_module[0].get_text().replace(' ', '').replace('/', ',').split(':')[1]
        else:
            actor = ''
        return actor

    # 读取演员ID
    def getActorId(self):
        actor_id = []
        re_obj = re.compile("[0-9]+")
        actor_module = self.bs_obj.find_all(attrs={"class": "actor"})
        if actor_module:
            for actor in actor_module[0].find_all(attrs={"rel": "v:starring"}):
                m = re.search(re_obj, actor.get("href"))
                if m is not None:
                    actor_id.append(int(m.group(0)))
        return str(actor_id)

    # 读取电影类型
    def getMovieType(self):
        types_module = self.bs_obj.find_all(attrs={"property":"v:genre"})
        movie_type = []
        for type in types_module:
            movie_type.append(type.get_text())
        return ','.join(movie_type)

    # 读取电影上映时间
    def getMovieDate(self):
        date_module = self.bs_obj.find_all(attrs={"property": "v:initialReleaseDate"})
        moviedate = ''
        if date_module:
            moviedate = date_module[0].get_text()
        return moviedate

    # 读取电影时长
    def getRunTime(self):
        runtime_module = self.bs_obj.find_all('span',attrs={"property":"v:runtime"})
        runtime = -1
        if runtime_module:
            runtime = int(runtime_module[0]["content"])
        return runtime

    # 读取电影概述
    def getSummary(self):
        summary_module = self.bs_obj.find_all('span',attrs={"property":"v:summary"})
        movie_summary = ''
        if summary_module:
            movie_summary = summary_module[0].get_text()
            movie_summary = str(movie_summary).replace(' ', '').replace('\n', '').replace('\t', '')
        return movie_summary if len(movie_summary) < 5000 else movie_summary[:4999]

    # 获取推荐列表
    def getRecomment(self):
        Recomment_lists = self.bs_obj.find(attrs={"class": "recommendations-bd"}).find_all("a")
        relatedlists = []
        for list in Recomment_lists:
            url = list["href"].replace("/?from=subject-page", "")
            relatedlists.append(url)
        return relatedlists

    def is_empty(self):
        if self.bs_obj is None or (self.bs_obj and self.getMovieName() == ''):
            return True
        else:
            return False

if __name__ == '__main__':
    url = "https://movie.douban.com/subject/25864124"
    crawler = Crawler_single(url)
    #print crawler
    print "MovieName:", crawler.getMovieName()
    print "Keyword:", crawler.getKeyword()
    print "RatingNum:", crawler.getRatingNum()
    print "Director:", crawler.getDirector()
    print "DirectorID:", crawler.getDirectorId()
    print "Actors:", crawler.getActor()
    print "ActorIDs:", crawler.getActorId()
    print "Movietype:", crawler.getMovieType()
    print "MovieDate:", crawler.getMovieDate()
    print "Runtime:", crawler.getRunTime()
    print "Summary:", crawler.getSummary()
    print "RecommentLists:", crawler.getRecomment()
