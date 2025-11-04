from flask_restful import Resource
from helpers.stats import *


class StatsApi(Resource):
    def post(self, route):
        if route == "create_stats":
            return CreateStats()
        
    
    def get(self, route):
        if route == "get_all_stats":
            return GetAllStats()
