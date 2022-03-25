from custom_classes.scraper import Scraper
from custom_classes.sortinfo import SortInfo

company = input('Hi, please input the Symbol of the company you wish to scrape: ')
original_link = f"https://finance.yahoo.com/quote/{company}/history?p={company}"

dict_stock_info = {
    'Date': [],
    'Open': [],
    'High': [],
    'Low': [],
    'Close': [],
    'Adj_close': [],
    'Volume': []
}

scrape_company = Scraper()
scrape_company.create_req(original_link)
scrape_company.store_info(dict_stock_info)
scrape_company.close_req()

save_files = SortInfo(dict_stock_info)
save_files.create_csv(company)
save_files.create_spreadsheet(company)

