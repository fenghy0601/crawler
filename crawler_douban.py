#coding:utf-8
from bs4 import BeautifulSoup
from urllib2 import urlopen
from urllib2 import HTTPError
import time
import random
import datetime

def getContent(url):

    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html,"html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None

    ID = url.split('/')[-1]

    if (title.get_text().replace('\n','')):
        moviename = title.get_text().replace('\n','')
    else:
        moviename = ''

    if (bsObj.find_all(attrs={"name":"keywords"})):
        keywords = bsObj.find_all(attrs={"name":"keywords"})[0]["content"]
    else:
        keywords = ''

    if (bsObj.find_all(attrs={"class":"ll rating_num","property":"v:average"})):
        rating_num = bsObj.find_all(attrs={"class":"ll rating_num","property":"v:average"})[0].get_text()
    else:
        rating_num = ''

    if (bsObj.find_all(attrs={"rel":"v:directedBy"})):
        director =  bsObj.find_all(attrs={"rel":"v:directedBy"})[0].get_text()
    else:
        director =''

    if (bsObj.find_all(attrs={"class":"actor"})):
        actor = bsObj.find_all(attrs={"class":"actor"})[0].get_text().replace(' ','').replace('/',',').split(':')[1]
    else:
        actor = ''

    if (bsObj.find_all(attrs={"property":"v:genre"})):
        types = bsObj.find_all(attrs={"property":"v:genre"})
        movietype =[]
        for type in types:
            movietype.append(type.get_text())
    else:
        movietype =[]

    if (bsObj.find_all(attrs={"property":"v:initialReleaseDate"})):
        dte = bsObj.find_all(attrs={"property":"v:initialReleaseDate"})[0].get_text()
    else:
        dte = ''

    if (bsObj.find_all('span',attrs={"property":"v:runtime"})):
        runtime = bsObj.find_all('span',attrs={"property":"v:runtime"})[0]["content"]
    else:
        runtime = ''

    if (bsObj.find_all('span',attrs={"property":"v:summary"})):
        summary = bsObj.find_all('span',attrs={"property":"v:summary"})[0]
        movie_summary = summary.get_text().replace(' ', '').replace('\n', '').replace('\t', '')
    else:
        movie_summary = ''

    content = []
    content.append(ID)
    content.append(moviename)
    content.append(keywords)
    content.append(rating_num)
    content.append(director)
    content.append(actor)
    content.append(','.join(movietype))
    content.append(dte)
    content.append(runtime)
    content.append(movie_summary)


    lists = bsObj.find(attrs={"class":"recommendations-bd"}).find_all("a")
    relatedlists=[]
    for list in lists:
        relatedlists.append(list["href"].replace("/?from=subject-page",""))

    content.append(relatedlists)
    return content


url = "https://movie.douban.com/subject/22939161"
random.seed(datetime.datetime.now())
for i in range(200):
    while True:
        content = getContent(url)
        relatedlists = content[-1]
        if(content and relatedlists):
            break
    random.seed(datetime.datetime.now())
    index = random.randint(0, len(relatedlists) - 1)
    url = relatedlists[index]

    time.sleep(random.randint(1,5))
    print '|~|'.join(content[0:-2])

