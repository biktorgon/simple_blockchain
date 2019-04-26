from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from block import *


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        who = request.form['who']
        amount = request.form['amount']
        whom = request.form['whom']

        try:
            write_block_transact(who, amount, whom)
        except Exception as err:
            print(err)
        else:
            return redirect(url_for('index'))

    return render_template('index.html')


@app.route('/checking', methods=['GET'])
def check():
    results = check_blocks_hash()
    return render_template('index.html', results=results)


if __name__ == "__main__":
    app.run(debug=True)
