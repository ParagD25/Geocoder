# Geocoder 🌏
An application where one can upload a '.csv' file that has an address column that contains certain address and would get a '.csv' file in return that has Latitude and Longitude coordinates related to that address.

## Prerequisites 📋

You'll need [Git](https://git-scm.com) and [Python](https://www.python.org/) installed on your computer.

[![](https://camo.githubusercontent.com/2fb0723ef80f8d87a51218680e209c66f213edf8/68747470733a2f2f666f7274686562616467652e636f6d2f696d616765732f6261646765732f6d6164652d776974682d707974686f6e2e737667)](https://python.org)


## Framework Used 📁:

- [Pandas](https://pandas.pydata.org/) - To Create Table.
- [Geopy](https://pypi.org/project/geopy/) - To extract Coordinates from given Address.
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) - To create Web app.

## How To Use 🔧:

From your command line, first clone this repo:

```bash
# Clone this repository
$ git clone https://github.com/ParagD25/Geocoder/

# Go into the repository
$ cd Geocoder

# Remove current origin repository
$ git remote remove origin

# Create new virtual python environment
$ python3 -m venv venv

# Activate virtual python environment
$ source venv/bin/activate

# Install all the libraries/frameworks mentioned above

# Run Python file
$ "python stocks.py" - Visit the URL created in cmd to see the Website locally.
OR
Visit "https://geo-coder1.herokuapp.com/"

```

## Screenshots 📷:

<h3 align="center">Home Page -</h3>
<p align="center">
  <img src="https://github.com/ParagD25/Geocoder/blob/master/Images/home.png" alt="Heroku Home Page" width="100%">
</p>

<h3 align="center">Select a proper <em>.csv</em> File that contains <em>Address</em> Column -</h3>
<p align="center">
  <img src="https://github.com/ParagD25/Geocoder/blob/master/Images/select.png" alt="Heroku Selection Page" width="100%">
</p>

<h3 align="center">Result (You can also Download the Table that's been created) -</h3>
<p align="center">
  <img src="https://github.com/ParagD25/Geocoder/blob/master/Images/result.png" alt="Heroku Result Page" width="100%">
</p>

## Contributing ©️:

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
