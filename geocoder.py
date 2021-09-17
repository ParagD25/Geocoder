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
    global name_file

    if request.method=="POST":
        file=request.files['file']

        try:
            df=pd.read_csv(file)
            gc=Nominatim(user_agent='My_App')
            df["coordinates"]=df["Address"].apply(gc.geocode)
            df['Latitude'] = df['coordinates'].apply(lambda x: x.latitude if x != None else None)
            df['Longitude'] = df['coordinates'].apply(lambda x: x.longitude if x != None else None)
            df['Altitude'] = df['coordinates'].apply(lambda x: x.altitude if x != None else None)
            df=df.drop("coordinates",1)
            name_file=dt.datetime.now().strftime("uploads/%d-%m-%Y_%S"+".csv")
            df.to_csv(name_file,index=None)
            return render_template("home.html", text=df.to_html(), admin_management='download.html')

        except:
            return render_template("home.html", text="Please Include Address Column in your .csv file")

@app.route('/download/')
def download():
    return send_file(name_file,attachment_filename='Coordinates.csv',as_attachment=True)

if __name__=='__main__':
    app.run(debug=True)