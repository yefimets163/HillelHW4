from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def loginUser():
    if request.method == 'GET':
        pass
    else:
        pass
    return "<p>Login!</p>"

@app.route("/logout", methods = ['GET'])
def logout_userd():
    return "<p>Logout</p>"

@app.route("/register", methods = ['GET', 'POST'])
def register_user():
    return "Registration form"

@app.route("/user_page", methods = ['GET'])
def user_access():
    return "More functions"

@app.route("/currency", methods = ['GET', 'POST'])
def currency_converter():
    currency_list = [
        {'bank': 'A1', 'date': "2022-11-25", 'currency': 'UAH', 'buy_rate': 0.025, 'sale_rate': 0.023},
        {'bank': 'A1', 'date': "2022-11-25", 'currency': 'EUR', 'buy_rate': 0.9, 'sale_rate': 0.95},
        {'bank': 'A1', 'date': "2022-11-25", 'currency': 'USD', 'buy_rate': 1, 'sale_rate': 1},
        {'bank': 'A1', 'date': "2022-11-25", 'currency': 'GPB', 'buy_rate': 1.15, 'sale_rate': 1.2}
    ]

    if request.method == 'POST':
        user_bank = request.form['bank']
        user_currency_1 = request.form['currency_1']
        user_date = request.form['date']
        user_currency_2 = request.form['currency_2']
        buy_rate_1 = 1
        buy_rate_2 = 1
        sale_rate_1 = 1
        sale_rate_2 = 1
        for one_currency_info in currency_list:
            if user_bank == one_currency_info['bank'] and user_currency_1 == one_currency_info['currency'] \
                    and user_date == one_currency_info['date']:
                buy_rate_1 = one_currency_info['buy_rate']
                sale_rate_1 = one_currency_info['sale_rate']
            if user_bank == one_currency_info['bank'] and user_currency_2 == one_currency_info['currency'] \
                    and user_date == one_currency_info['date']:
                buy_rate_2 = one_currency_info['buy_rate']
                sale_rate_2 = one_currency_info['sale_rate']

        cur_exchange_buy = buy_rate_2 / buy_rate_1
        cur_exchange_sale = sale_rate_2 / sale_rate_1

        return render_template('currencyForm.html',
                               cur_exchange_buy = cur_exchange_buy,
                               cur_exchange_sale = cur_exchange_sale,
                               user_currency_1 = user_currency_1,
                               user_currency_2 = user_currency_2
                               )
    else:
        return render_template('currencyForm.html')


