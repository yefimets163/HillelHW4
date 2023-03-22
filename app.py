from flask import Flask, render_template
from flask import request
from requests import Session

from dbFunc import DBManager
from celeryWork import add
import al_db
import models_db
from sqlalchemy import select

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def login_user():
    if request.method == 'GET':
        with Session(al_db.engine) as session:
            query = select(models_db.Currency)
            result = session.execute(query).fetchall()
        return str(result)
    else:
        pass
    return "<p>Login!</p>"

@app.route("/logout", methods = ['GET'])
def logout_user():
    add.apply_async(args=(1, 2))

@app.route("/register", methods = ['GET', 'POST'])
def register_user():
    return "Registration form"

@app.route("/user_page", methods = ['GET'])
def user_access():
    return "More functions"



@app.route("/currency", methods = ['GET', 'POST'])
def currency_converter():
    if request.method == 'POST':


        user_bank = request.form['bank']
        user_currency_1 = request.form['currency_1']
        user_date = request.form['date']
        user_currency_2 = request.form['currency_2']

        with Session(al_db.engine) as session:
            statement_1 = select(models_db.Currency).filter_by(bank=user_bank,
                                                               currency=user_currency_1,
                                                               date_exchange=user_date)
            currency_1 = session.scalars(statement_1).first()

            statement_2 = select(models_db.Currency).filter_by(bank=user_bank,
                                                               currency=user_currency_2,
                                                               date_exchange=user_date)
            currency_2 = session.scalars(statement_2).first()


        buy_rate_1, sale_rate_1 = currency_1.buy_rate, currency_1.sale_rate
        buy_rate_2, sale_rate_2 = currency_2.buy_rate, currency_2.sale_rate
        cur_exchange_buy = round(buy_rate_2 / buy_rate_1, 2)
        cur_exchange_sale = round(sale_rate_2 / sale_rate_1, 2)

        return render_template('currencyForm.html',
                               cur_exchange_buy = cur_exchange_buy,
                               cur_exchange_sale = cur_exchange_sale,
                               user_currency_1 = user_currency_1,
                               user_currency_2 = user_currency_2
                               )
    else:
        return render_template('currencyForm.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
