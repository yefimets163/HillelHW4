from flask import Flask, render_template
from flask import request
import sqlite3

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
    con = sqlite3.connect("currencyData.db")
    cursor = con.cursor()

    if request.method == 'POST':
        user_bank = request.form['bank']
        user_currency_1 = request.form['currency_1']
        user_date = request.form['date']
        user_currency_2 = request.form['currency_2']

        res_1 = cursor.execute(f'SELECT buyRate, sellRate FROM currency WHERE bank="{user_bank}" and dateExchange="{user_date}" and currency="{user_currency_1}"')
        buy_rate_1, sale_rate_1 = res_1.fetchone()
        res_2 = cursor.execute(f'SELECT buyRate, sellRate FROM currency WHERE bank="{user_bank}" and dateExchange="{user_date}" and currency="{user_currency_2}"')
        buy_rate_2, sale_rate_2 = res_2.fetchone()

        cur_exchange_buy = round(buy_rate_2 / buy_rate_1, 2)
        cur_exchange_sale = round(sale_rate_2 / sale_rate_1, 2)

        cursor.close()
        con.close()
        return render_template('currencyForm.html',
                               cur_exchange_buy = cur_exchange_buy,
                               cur_exchange_sale = cur_exchange_sale,
                               user_currency_1 = user_currency_1,
                               user_currency_2 = user_currency_2
                               )
    else:
        return render_template('currencyForm.html')


