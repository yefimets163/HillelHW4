import os
import datetime
from celery import Celery

import al_db
import models_db
from sqlalchemy import select
from sqlalchemy.orm import Session
import requests_bank

rabbit_host = os.environ.get('RABBIT_HOST', 'localhost')
app = Celery('celeryWork', broker = f'pyamqp://guest@{rabbit_host}//')

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, get_bank_data_task.s(), name='add every 10')

@app.task
def get_bank_data_task():
    requests_bank.get_PrivatBank_data()
    return True
