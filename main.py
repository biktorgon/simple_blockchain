from flask import Flask
from flask import render_template
from flask import request
from block import *


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        who = request.form['who']
        amount = request.form['amount']
        whom = request.form['whom']

        write_file_transact(who, amount, whom)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)