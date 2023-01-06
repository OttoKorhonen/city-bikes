'''imported modules'''
from flask import Flask, request
import addresses
import requests
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = ''
app.config['SQLALCHEMY_DATABASE_URI'] = ''
db = SQLAlchemy(app)

def fetch_data():
    '''function fetches data'''
    url = addresses.dataset_address
    data = requests.get(url, timeout=10)
    return data.text

def parse_data():
    '''function parses out wanted data i.e. too short distances 
    (less than 10 seconds or less than 10 metres)'''

def insert_data_into_db():
    '''function inserts data into db'''


class Station(db.Model):
    '''class for station'''
    __tablename__ = 'kaupunkipyoraasema'
    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String, nullable=True)
    namn = db.Column(db.String, nullable=True)
    name = db.Column(db.String, nullable=True)
    osoite = db.Column(db.String, nullable=True)
    adress = db.Column(db.String, nullable=True)
    kaupunki = db.Column(db.String, nullable=True)
    stad = db.Column(db.String, nullable=True)
    operaattori = db.Column(db.String, nullable=True)
    kapasiteetti = db.Column(db.Integer, nullable=True)
    x_coord = db.Column(db.Float, nullable=True)
    y_coord = db.Column(db.Float, nullable=True)

@app.route('/', methods=['GET'])
def index():
    '''function returns hello world text'''
    data = fetch_data()
    return f'Hello world!\n{data}'

@app.route('/station', methods=['GET', 'POST'])
def station():
    '''function returns single station info'''
    s = request.get_json()
    print(s)
    return s

@app.route('/stations/all', methods=['GET'])
def station_list():
    '''function returns list of stations'''

@app.route('/journeys', methods=['GET'])
def journeys():
    '''function returns list of journeys'''

if __name__ == '__main__':
    app.run(debug=True)

