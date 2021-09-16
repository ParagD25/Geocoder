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
        file=request.files['file']

        try:
            data=pd.read_csv(file)
            coord=Nominatim()
            data['Coordinates']=data['Address'].apply(coord.geocode)
            data['Latitude']=data['Coordinates'].apply(lambda lat:lat.latitude if lat!=None else None)
            data['Longitude']=data['Coordinates'].apply(lambda lon:lon.latitude if lon!=None else None)
            data=data.drop('Coordinates',1)
            name_of_file=dt.datetime.now().strftime("uploads/%m_%d_%M_%s"+".csv")
            data.to_csv(name_of_file,index=None)
            return render_template('home.html', text=data.to_html(), btn='download.html')

        except:
            return render_template('home.html',text='Please Enter Address Column in your csv file.')

@app.route('/download/')
def download():
    return send_file(name_of_file,attachment_filename='Coordinates.csv',as_attachment=True)

if __name__=='__main__':
    app.run(debug=True)