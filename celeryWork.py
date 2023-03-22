import os
import datetime
from celery import Celery

import al_db
import models_db
from sqlalchemy import select
from sqlalchemy.orm import Session

rabbit_host = os.environ.get('RABBIT_HOST', 'localhost')
app = Celery('celeryWork', broker = f'pyamqp://guest@{rabbit_host}//')

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, add.s(x=2, y=4), name='add every 10')

@app.task
def add(x, y):
    print(x + y)
    record1 = models_db.Currency(bank="GGG", currency='USD', dateExchange='2020-01-01', buyRate=1.1, sellRate=1.2)
    with Session(al_db.engine) as session:
        session.add(record1)
        session.commit()
