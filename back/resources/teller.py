from flask_restful import Resource
import json
from helpers.teller import *
from flask import request


class TellerApi(Resource):
    def post(self, route):
        if route == "create":
            return CreateTeller()
        
        if route == "login":
            return LoginTeller() 
        
        if route == "readsingle":
            return ReadSingleTeller() 
        
        if route == "forgot_password":
            return ForgotPassword() 
        
        if route == "save_new_password":
            return SaveNewPassword() 

        if route == "update_teller":
            return UpdateTeller()        
    
    def get(self, route):
        if route == "readall":
            return ReadAllTeller()

            
    
    # def delete(self, route):
    #      if route == "delete":
    #         return DeleteTeller()
         
    # def patch(self, route):
    #     if route == "update":
    #         return UpdateTeller()
        