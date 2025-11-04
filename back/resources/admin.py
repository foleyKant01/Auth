from ipaddress import ip_address
from flask_restful import Resource
from helpers.admin import *
from flask import request


class AdminApi(Resource):
    def post(self, route):
        if route == "create":
            return CreateAdmin() 
        
        if route == "login":
            return LoginAdmin()
        
        if route == "forgot_password":
            return ForgotPassword() 
        
        if route == "save_new_password":
            return SaveNewPassword()
        
        if route == "update_admin":
            return UpdateAdmin()


        
    
    def get(self, route):
        if route == "readall":
            return ReadAllAdmin