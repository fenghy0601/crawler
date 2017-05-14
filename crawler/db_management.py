#coding:utf-8
import pymysql
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class dbManagement():
    def __init__(self):
        self.conn = self.getConn()

    @staticmethod
    def getConn():
        config = {'host': '127.0.0.1',
                  'port': 3306,
                  'user': 'root',
                  'password': 'root',
                  'db': 'crawler',
                  'charset': 'utf8'
                  }
        return pymysql.connect(**config)

    def insert_data(self, id, name, keyword, ratingnum, director, actor, movietype, moviedate, runtime, summary):
        with self.conn.cursor() as cursor:
            time = datetime.datetime.now()
            sql = "insert into movieInfo (id, name, keywords, ratingnum, director, actor, movietype, moviedate, \
        runtime, summary, create_time, update_time) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            # cursor.execute(sql,(12,'1','q',3.2,'q','a','a','a',123,'a'))
            cursor.execute(sql, (id, name.encode('utf-8'), keyword, ratingnum, director, actor, movietype, \
                        moviedate, runtime, summary, time, time))
        self.conn.commit()

    def has_id(self, id):
        with self.conn.cursor() as cursor:
            sql = "select * from movieinfo where id = %s limit 1"
            cursor.execute(sql, id)
        return cursor.fetchone()

    def show_list(self):
        with self.conn.cursor() as cursor:
            sql = "select id from movieinfo"
            cursor.execute(sql)
        return cursor.fetchone()

if __name__ == '__main__':
    #dbManagement().insert_data(3, 'name', 'keyword', 4, 'director', 'actor', 'movietypr', 'mociedate', 100, '')
    #res = dbManagement().has_id(2)
    res = dbManagement().show_list()
    print res