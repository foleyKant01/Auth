from ipaddress import ip_address
from flask_restful import Resource
from helpers.historiques import *


class HistoriquesApi(Resource):
    def post(self, route):
        if route == "save_historique":
            return SaveHistorique()
        
        if route == "read_all_historique_by_user":
            return ReadAllHistoriqueByUser()
        
        if route == "delete_historiques":
            return DeleteHistoriques()
        