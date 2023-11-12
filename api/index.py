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
        form_data = request.form
        if info.use_characteristics == '1':
           placeholders.append(info.characteristics.article)
        else:
           placeholders.append(info.code)
        if stock.stock - stock.stock_reserved == 0:
           placeholders.append('FALSE')
        else:
           placeholders.append('TRUE')
        placeholders.append(info.title + ' ' +  info.characteristics.title)
        
        return render_template('data.html',form_data = form_data)
