from flask import Flask
from flask_restful import Api
from customerresources import Employess

app = Flask(__name__)

app.config.from_pyfile('customerdbconfigure.py')

api = Api(app)

api.add_resource(Employess,'/customer/all')


if __name__ == '__main__':
    app.run(debug=True)