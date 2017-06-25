# codingLutf-8
from crawler_ownet import CrawlerOWNet
import traceback

class crawlerMain:
    def __init__(self, choose_list):
        self.list = choose_list

    def begin_crawler(self):
        choose_list = self.list
        for code in choose_list:
            preurl = 'zs' + str(code) if code[0] == '0' else 'sz' + str(code)
            url = 'http://quote.eastmoney.com/' + preurl + '.html'
            print url
            try:
                crawler_obj = CrawlerOWNet(url)
                print crawler_obj.get_basic_element()
                print crawler_obj.get_id()
                print crawler_obj.get_code()
            except:
                print traceback.print_exc()
        return None




if __name__ == '__main__':
    list = ['000010', '600001']
    main_obj = crawlerMain(list).begin_crawler()