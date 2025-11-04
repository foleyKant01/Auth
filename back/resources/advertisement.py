from flask_restful import Resource, Api
import json
from helpers.advertisement import *
from flask import request


class AdvertisementApi(Resource):
    def post(self, route):
        if route == "createadvertisement":
            return CreateAdvertisement()
        
        if route == "readsingleadvertisement":
            return ReadSingleAdvertisement()
        
        if route == "updateadvertisement":
            return UpdateAdvertisement()
        
        if route == "deleteadvertisement":
            return DeleteAdvertisement()
    
    def get(self, route):
        if route == "readalladvertisement":
            return ReadAllAdvertisement()


