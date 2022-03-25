from bs4 import BeautifulSoup
import requests


class Scraper:

    def __init__(self):
        self.raw_dates = None
        self.divs = None
        self.soup = None
        self.req = None
        self.session = None

    def create_req(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/99.0.4844.74 Safari/537.36 '
        }
        self.session = requests.session()
        self.req = self.session.get(url, headers=headers)
        self.soup = BeautifulSoup(self.req.content, 'lxml')

    def store_info(self, dict_stock):
        self.raw_dates = self.soup.findAll('tr')

        for raw_date in self.raw_dates[1:100]:
            dict_stock['Date'].append(raw_date.findAll('td')[0].text)
            dict_stock['Open'].append(raw_date.findAll('td')[1].text)
            dict_stock['High'].append(raw_date.findAll('td')[2].text)
            dict_stock['Low'].append(raw_date.findAll('td')[3].text)
            dict_stock['Close'].append(raw_date.findAll('td')[4].text)
            dict_stock['Adj_close'].append(raw_date.findAll('td')[5].text)
            dict_stock['Volume'].append(raw_date.findAll('td')[6].text)

    def close_req(self):
        self.session.close()

