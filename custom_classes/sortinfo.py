import pandas as pd


class SortInfo:

    def __init__(self, dict_stock, total_crypto):
        self.dataframe = pd.DataFrame(dict_stock)
        total_crypto.update(dict_stock)

    @staticmethod
    def create_csv(total_crypto):
        final_dataframe = pd.DataFrame(total_crypto)
        final_dataframe.to_csv(f"general_cryptos.csv", index=False, header=True)

    def create_spreadsheet(self, crypto, spreadsheet_writer):
        self.dataframe.to_excel(spreadsheet_writer, sheet_name=f'{crypto}', index=False,
                                header=True)
