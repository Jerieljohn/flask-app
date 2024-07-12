from flask import Flask,render_template
from database import get_data


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webtt')
def webt():
    data = get_data()
    return render_template('webt.html',data=data)
    
@app.route('/mycontacts')
def mycontacts():
    return render_template('mycontacts.html')

if __name__=="main":
    app.run()
