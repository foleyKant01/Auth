from flask_restful import Resource
from helpers.reports import *
from flask import request


class ReportsApi(Resource):
    def post(self, route):
        if route == "reports_teller":
            return ReportsTeller()
        