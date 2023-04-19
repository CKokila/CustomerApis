from flask import request
from flask_restful import Resource
from customermodels import allEmployees,getAllProducts,getProductById,home

class Employess(Resource):
    def get(self):
        employees = allEmployees()
        return employees
    
class Home(Resource):
    def get(self,id):
        productid = home(id)
        return productid    

class Products(Resource):
    def get(self):
        products = getAllProducts()
        return products
    

class ProductById(Resource):
    def get(self,id):
        productID = getProductById(id)
        return productID