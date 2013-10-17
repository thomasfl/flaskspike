import os
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def test_entry():
    return render_template('index.html')

@app.route('/calculate', methods=['GET','POST'])
def hello():
    result = -1
    try:
        result = int(request.form['a']) + int(request.form['b'])
    except Exception:
        pass
    return render_template('index.html', result=result)

if(not(os.environ.has_key("PRODUCTION_MODE"))):
    app.run(debug=True)
