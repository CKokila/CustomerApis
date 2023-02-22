from flask import request
from flask_restful import Resource
from customermodels import allEmployees

class Employess(Resource):
    def get(self):
        employees = allEmployees()
        return employees