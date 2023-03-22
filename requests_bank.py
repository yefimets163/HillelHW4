import datetime

import requests

import al_db
import models_db
from sqlalchemy.orm import Session


def get_PrivatBank_data():
    current_date = datetime.datetime.now().strftime("%d.%m.%Y")
    db_date = datetime.datetime.now().strftime("%Y.%m.%d")

    r = requests.get(f'https://api.privatbank.ua/p24api/exchange_rates?json&date={current_date}')

    currency_info = r.json()
    saleRate_USD = 0
    purchaseRate_USD = 0
    saleRate_UAH = 0
    purchaseRate_UAH = 0
    
    for c in currency_info['exchangeRate']:
        if c['currency'] == 'USD':
            saleRate_USD = c['saleRate']
            purchaseRate_USD = c['purchaseRate']

    with Session(al_db.engine) as session:
        for c in currency_info['exchangeRate']:
            currency_name = c['currency']
            if c.get('saleRate'):
                print(c)
                saleRate_currency = c['saleRate'] / saleRate_USD
                purchaseRate_currency = c['purchaseRate'] / purchaseRate_USD
                print(f'{currency_name} {saleRate_currency} {purchaseRate_currency}')
                record = models_db.Currency(
                    bank='PrivatBank',
                    currency=currency_name,
                    dateExchange=db_date,
                    buyRate=purchaseRate_currency,
                    sellRate=saleRate_currency
                )
                session.add(record)
                session.commit()
                
    for c in currency_info['exchangeRate']:
        if c['currency'] == 'UAH':
            saleRate_UAH = c['saleRate']
            purchaseRate_UAH = c['purchaseRate']
            
    with Session(al_db.engine) as session:
        for c in currency_info['exchangeRate']:
            currency_name = c['currency']
            if c.get('saleRate'):
                print(c)
                saleRate_currency = c['saleRate'] / saleRate_UAH
                purchaseRate_currency = c['purchaseRate'] / purchaseRate_UAH
                print(f'{currency_name} {saleRate_currency} {purchaseRate_currency}')
                record = models_db.Currency(
                    bank='PrivatBank',
                    currency=currency_name,
                    dateExchange=db_date,
                    buyRate=purchaseRate_currency,
                    sellRate=saleRate_currency
                )
                session.add(record)
                session.commit()
