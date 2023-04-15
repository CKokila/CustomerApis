from flask import Flask
from flask_restful import Api
from customerresources import Employess,Products,ProductById,Home

app = Flask(__name__)


app.config.from_pyfile('customerdbconfigure.py')

api = Api(app)

api.add_resource(Employess,'/customer/all')
api.add_resource(Products,"/products")
api.add_resource(ProductById,"/id")
api.add_resource(Home,"/id/")



if __name__ == '__main__':
    app.run(host = '0.0.0.0',port=5000,debug=True)
    
