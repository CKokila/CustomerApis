from flask import Flask
from flask_restful import Api
from customerresources import Employess,Products

app = Flask(__name__)


app.config.from_pyfile('customerdbconfigure.py')

api = Api(app)

api.add_resource(Employess,'/customer/all')
api.add_resource(Products,"/products")


if __name__ == '__main__':
    app.run(host = '0.0.0.0',port=5000,debug=True)
    
