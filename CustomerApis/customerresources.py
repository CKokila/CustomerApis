from flask import request
from flask_restful import Resource
from customermodels import allEmployees,getAllProducts,getProductById,home

class Employess(Resource):
    def get(self):
        employees = allEmployees()
        return employees
    
class Home(Resource):
    def get(self):
        productid = home(self)
        return productid    

class Products(Resource):
    def get(self):
        products = getAllProducts()
        return products
    

class ProductById(Resource):
    def get(self):
        productID = getProductById()
        return productID