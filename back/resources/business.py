from flask_restful import Resource
from helpers.business import *


class BusinessApi(Resource):
    def post(self, route):
        if route == "createbusiness":
            return CreateBusiness()

        if route == "insertallbusiness":
            return InsertAllBusiness()

        if route == "search":
            return search()
        
        if route == "readsinglebusiness":
            return ReadSingleBusiness()  
        
        if route == "readsinglebusinessbycategories":
            return ReadAllBusinessByCategories() 
            
        if route == "readallbusinessbyteller":
            return ReadAllBusinessByTeller()
        
        if route == "searchbusinessbycategorie":
            return SearchBusinessByCategorie()
        
        if route == "updatebusiness":
            return UpdateBusiness()

        
    def get(self, route):
        if route == "readallbusiness":
            return ReadAllBusiness()
        
        
    def delete(self, route):
        if route == "deletebusiness":
            return DeleteBusiness()

         
    def patch(self, route):

        
        if route == "updatestatusbusiness":
            return UpdateStatusBusiness()