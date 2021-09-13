import pandas
from flask import Flask,render_template,send_file,request
from geopy.geocoders import Nominatim

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sucess',methods=['POST'])
def sucess():
    return render_template('home.html')

@app.route('/download')
def download():
    return send_file()

if __name__=='__main__':
    app.run(debug=True)