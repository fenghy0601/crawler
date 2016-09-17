#coding:utf-8
from bs4 import BeautifulSoup
from urllib2 import urlopen
from urllib2 import HTTPError
import time
import random
import datetime
import pymysql

#get the content from douban movie
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


def insertdata(content):
    id = content[0]
    name = content[1]
    keyword = content[2]
    ratingnum = content[3]
    director = content[4]
    actor = content[5]
    movietype = content[6]
    moviedate = content[7]
    runtime = content[8]
    summary = content[9]

    config={'host':'127.0.0.1',
            'port':3306,
            'user':'root',
            'password':'root',
            'db':'crawler',
            'charset':'utf8mb4'
            }
    conn = pymysql.connect(**config)
    try:
        with conn.cursor() as cursor:
            sql="insert into movieInfo (id, name, keywords, ratingnum, director, actor, movietype, moviedate, runtime, summary) \
  values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            #cursor.execute(sql,(12,'1','q',3.2,'q','a','a','a',123,'a'))
            cursor.execute(sql,(id, name.encode('utf-8'), keyword, ratingnum, director, actor, movietype, moviedate, runtime, summary))
        conn.commit()
    finally:
        conn.close()
    print '|~|'.join(content[0:-2])


url = "https://movie.douban.com/subject/22939161"
random.seed(datetime.datetime.now())
chooselist=[]
crawlerlist=[]
for i in range(1000):
    crawlerlist.append(url)
    while True:
        content = getContent(url)
        if(content):
            relatedlists = content[-1]
            for list in relatedlists:
                if list not in chooselist and list not in crawlerlist:
                    chooselist.append(list)
            if(relatedlists):
                break
            
    random.seed(datetime.datetime.now())
    index = random.randint(0, len(chooselist) - 1)
    url = chooselist[index]
    chooselist.remove(url)
    print url
    print 'num of choose:',len(chooselist),'  has been crawed',len(crawlerlist)    

    time.sleep(random.randint(1,5))
    insertdata(content)


