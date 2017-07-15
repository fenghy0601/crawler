import lxml.html
import json
import crawler_tools

class Crawler_fund:
    def __init__(self, url):
        self.html = crawler_tools.download(url)

if __name__ == '__main__':
    fund1 = Crawler_fund('http://fund.eastmoney.com/trade/pg.html')
    tree = lxml.html.fromstring(fund1.html)
    funds = tree.cssselect('table#tblite_pg > tbody > tr')
    for single_fund in funds:
        id = single_fund[0].text_content()
        name = single_fund.cssselect('td.fname')[0].text_content()
        fb = single_fund.cssselect('td > span.fb')[0].text_content()
        date = single_fund.cssselect('td > span.date')[0].text_content()
        num = []
        for num_attr in single_fund.cssselect('td[class*=num]'):
            num.append(num_attr.text_content())
        start_num = single_fund.cssselect('div.l > a')[0].text_content()
        cost_rate = single_fund.cssselect('div.r')[0].text_content()
        print id, name, fb, date, num, start_num, cost_rate
