from flask import request
from flask_restful import Resource
from customermodels import allEmployees,getAllProducts

class Employess(Resource):
    def get(self):
        employees = allEmployees()
        return employees
    

class Products(Resource):
    def get(self):
        products = getAllProducts()
        return products