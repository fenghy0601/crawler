#!/usr/bin/env python
#-*-coding:utf-8 -*-

from urllib2 import urlopen
from urllib2 import HTTPError
from bs4 import BeautifulSoup 

def getTitle(url):
   try:
      html = urlopen(url)
   except HTTPError as e:
      return None
   try:
      bsObj = BeautifulSoup(html.read())
      title = bsObj.body.h1
   except AttributeError as e:
      return None
#   return title
   return title.get_text()

title = getTitle("http://www.douban.com")
if title == None:
  print("Title counld not be found")
else:
  print(title)
