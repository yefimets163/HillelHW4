from sqlalchemy import Column, Integer, String, Float
from al_db import Base

class Currency(Base):
    __tablename__ = 'currency'
    id = Column(Integer, primary_key=True, unique=True)
    bank = Column(String(50))
    currency = Column(String(120))
    dateExchange = Column(String(120))
    buyRate = Column(Float)
    sellRate = Column(Float)

    def __init__(self, bank, currency, dateExchange, buyRate, sellRate):
        self.bank = bank
        self.currency = currency
        self.dateExchange = dateExchange
        self.buyRate = buyRate
        self.sellRate = sellRate

    def __repr__(self):
        return f'<User {self.name!r}>'
