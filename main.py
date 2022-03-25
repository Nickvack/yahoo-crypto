from custom_classes.scraper import Scraper
from custom_classes.sortinfo import SortInfo
import pandas as pd
import time
#
#
"""
The following are the following classes that will store and manipulate the information from the different websites.
"""
total_dict_crypto_info = {
        'Date': [],
        'Open': [],
        'High': [],
        'Low': [],
        'Close': [],
        'Adj_close': [],
        'Volume': []
    }
list_crypt = []
page_num = range(0, 300, 100)
crypto_list_link = 'https://finance.yahoo.com/cryptocurrencies/?count=100&offset='
"""
To initialize the program. 
"""
scrape_crypto = Scraper()
[scrape_crypto.get_crypto_list(crypto_list_link+str(page), list_crypt) for page in page_num]
writer = pd.ExcelWriter('Cryptocurrencies.xlsx', engine='xlsxwriter')

for crypt in list_crypt:
    dict_crypto_info = {
        'Date': [],
        'Open': [],
        'High': [],
        'Low': [],
        'Close': [],
        'Adj_close': [],
        'Volume': []
    }
    original_link = f"https://finance.yahoo.com/quote/{crypt}/history?p={crypt}"
    scrape_crypto.create_req(original_link)
    scrape_crypto.store_info(dict_crypto_info)
    scrape_crypto.close_req()

    save_files = SortInfo(dict_crypto_info, total_dict_crypto_info)
    save_files.create_spreadsheet(crypt, writer)
    print(f'{crypt} succesful')
    time.sleep(1)

writer.save()
dict_crypto_info = {}

save_files = SortInfo(dict_crypto_info, total_dict_crypto_info)
save_files.create_csv(total_dict_crypto_info)

