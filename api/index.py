from flask import Flask,render_template,request
 
app = Flask(__name__)
 
@app.route('/form')
def form():
    return render_template('form.html')
 
@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        info = request.form['info']
        prices = request.form['info']
        return render_template('data.html',info = info, prices = prices)
