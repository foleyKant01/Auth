from flask_restful import Resource
import json
from helpers.categories import *
from flask import request


class CategoriesApi(Resource):
    def post(self, route):
        if route == "createcategorie":
            return CreateCategories() 
    
        # if route == "readsinglecategorie":
        #     return ReadSingleCategories()
        
        if route == "deletecategorie":
            return DeleteCategories()
        
        if route == "insert_all_categories":
            return InsertAllCategories()
        
        if route == "updatecategorie":
            return UpdateCategories()
        
        
        
    def get(self, route):
        if route == "readallcategorie":
            return ReadAllCategories()
