'''imported modules'''
from flask import Flask

app = Flask(__name__)
app.secret_key = 'zah1Raim3me4ainoo5loogo0beshoh'

@app.route('/', methods=['GET'])
def index():
    return 'Hello world!'

if __name__ == '__main__':
    app.run(debug=True)
