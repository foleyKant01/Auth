from ipaddress import ip_address
from flask_restful import Resource
from helpers.users import *
from flask import request


class UsersApi(Resource):
    def post(self, route):
        if route == "create":
            return CreateUser()
        
        if route == "login":
            return LoginUser()
        
        if route == "localisation":
            return SaveLocation()
        
        if route == "test":
            return test()
        
        if route == "forgot_password":
            return ForgotPassword()
        
        if route == "save_new_password":
            return SaveNewPassword()
    
    def get(self, route):
        if route == "readall":
            return ReadAllUser()
        if route == "readsingle":
            return ReadSingleUser()

        # if route == "localisation":
        #     return Geolocate()
            
    
    def delete(self, route):
         if route == "delete":
            return DeleteUser()
         
    def patch(self, route):
        if route == "update":
            return UpdateUser()
        