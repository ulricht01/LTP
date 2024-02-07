from flask import Flask
from flask import render_template, redirect, jsonify, request, flash
import json
import database, app_logic
import os

app = Flask(__name__)

app.config['SECRET_KEY'] ="super secret key"

#Vytvoření db a tabulek
database.vytvor_db()
database.vytvor_tabulky()


# Registrace přes Flaskové rozhraní a následné vytvoření whitelistu z databáze
@app.route('/', methods=['GET', 'POST'])
def registrace():
    if request.method == "POST":
        uuid = request.form['uuid']
        jmeno = request.form['uzivatel']
        heslo = request.form['heslo']
        check = database.check_uzivatel(jmeno)
        if check is None:
            database.pridej_uzivatele(uuid, jmeno, heslo)
            flash("Byl jsi úspěšně přidán!", 'mess_success')
            os.chdir("..")
            os.chdir('minecraft-data')
            app_logic.create_whitelist()
        else:
            flash("Uživatel již existuje!", 'mess_error')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)