import pandas as pd


class SortInfo:

    def __init__(self, dict_stock):
        self.dataframe = pd.DataFrame(dict_stock)

    def create_csv(self, company):
        self.dataframe.to_csv(f"Stocks_{company}.csv", index=False, header=True)

    def create_spreadsheet(self, company):
        self.dataframe.to_excel(f"Stocks_{company}.xlsx", index=False, header=True)

