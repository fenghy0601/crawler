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

class CrawlerDisplay:
    def __init__(self):
        self.url = 'https://movie.douban.com/cinema/nowplaying/shanghai/'
        self.bs_obj = self.__getContent(self.url)

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

    def get_display_list(self):
        display_list = []
        list_module = self.bs_obj.find_all(attrs={"class": ["list-item", "list-item hidden"]})
        for list in list_module:
            id = list['id']
            if list['id'] is not None:
                display_list.append("https://movie.douban.com/subject/" + str(id))
        return display_list

if __name__ == "__main__":
    movie_list = CrawlerDisplay().get_display_list()
    print len(movie_list)
    print movie_list