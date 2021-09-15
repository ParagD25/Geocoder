import datetime as dt
import pandas as pd
from flask import Flask,render_template,send_file,request
from geopy.geocoders import Nominatim

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/success',methods=['POST'])
def success():
    global name_of_file
    if request.method=="POST":
        csv_file=request.files['file']

        try:
            data=pd.read_csv(csv_file)
            coord=Nominatim()
            data['Coordinates']=data['Address'].apply(coord.geocode)
            data['Latitude']=data['Coordinates'].apply(lambda lat:lat.latitude if lat!=None else None)
            data['Longitude']=data['Coordinates'].apply(lambda lon:lon.latitude if lon!=None else None)

        except:
            pass
    return render_template('home.html')

@app.route('/download')
def download():
    return send_file()

if __name__=='__main__':
    app.run(debug=True)