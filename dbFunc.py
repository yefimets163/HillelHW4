import sqlite3
import datetime

class DBManager:
    def __enter__(self):
        self.con = sqlite3.connect("currencyData.db")
        self.cursor = self.con.cursor()
        return self

    def __exit__(self,a,b,c):
        self.cursor.close()
        self.con.close()

    def getData(self, query):
        res_1 = self.cursor.execute(query)
        result = res_1.fetchone()
        return result

    def writeData(self, query):
        self.cursor.execute(query)
        self.con.commit()



def generateData():
    date = [
        {'bank':'a1', 'currency': 'UAH', 'buyRate': 0.023, 'sellRate': 0.025},
        {'bank':'a1', 'currency': 'USD', 'buyRate': 1, 'sellRate': 1},
        {'bank':'a1', 'currency': 'EUR', 'buyRate': 0.9, 'sellRate': 0.95},
        {'bank':'a1', 'currency': 'GBP', 'buyRate': 1.15, 'sellRate': 1.2}
            ]

    with DBManager() as db:
        for el in date:
            bank = el['bank']
            currency = el['currency']
            buyRate = el['buyRate']
            sellRate = el['sellRate']
            dateExchange = datetime.datetime.now().strftime('%Y-%m-%d')
            query = f'INSERT INTO currency (bank, currency, dateExchange, buyRate, sellRate) VALUES ("{bank}", "{currency}", "{dateExchange}", {buyRate}, {sellRate})'
            db.writeData(query)
