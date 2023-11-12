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
        placeholders.append(images)
        if prices.price_type:
           placeholders.append(prices.price)
        else:
           placeholders.append('')
        placeholders.append(info.properties[9].values.value)
        placeholders.append(info.assignments.trademark.article_title)
        if info.use_characteristics == '1':
           placeholders.append(info.characteristics.article)
        else:
           placeholders.append(info.code)
        placeholders.append(info.description + '/nДля сборки комплекта Вам дополнительно необходимо приобрести :')
        placeholders.append(assignments.videos)
        return render_template('data.html',form_data = form_data)
