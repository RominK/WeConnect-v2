from flask import Flask, jsonify, Blueprint

from flask_restful import Resource, abort, Api, reqparse

from models import Business

Businesses = {
    1: Business('Buz1', 'short description', 1, 'cat1', 'loc1').__dict__,
    2: Business('Buz2', 'short description2', 2, 'cat2', 'loc2').__dict__,
    3: Business('Buz3', 'short description3', 3, 'cat3', 'loc3').__dict__
}


def abort_if_business_doesnt_exist(business_id):
    if business_id not in Businesses:
        abort(404, message="Business {} doesn't exist".format(business_id))


class Business(Resource):
    """
    retrieve one business
    delet a business
    update a business
    """

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'name',
            required=True,
            help='No name provided',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'description',
            required=True,
            help='No Description provided',
            location=['form', 'json']
        )

        self.reqparse.add_argument(
            'owner_id',
            required=True,
            help='No owner id provided',
            location=['form', 'json']
        )
        
        self.reqparse.add_argument(
            'category',
            required=True,
            help='No category provided',
            location=['form', 'json']
        )

        self.reqparse.add_argument(
            'location',
            required=True,
            help='No location provided',
            location=['form', 'json']
        )
        super().__init__()

    def get(self, businessId):
        abort_if_business_doesnt_exist(businessId)
        return jsonify(Businesses[businessId])

    def delete(self, businessId):
        abort_if_business_doesnt_exist(businessId)
        del Businesses[businessId]
        return '', 204

    def put(self, businessId):
        args = self.reqparse.parse_args()
        business = Business(**args)
        Businesses[businessId] = business
        return jsonify(business), 201


class BusinessList(Resource):
    """
    List all businesses
    Add a business to the list of businesses
    """

    def get(self):
        return jsonify(Businesses)

    def post(self):
        args = reqparse.parse_args()
        businessId = int(max(Businesses.keys())+1)
        Businesses[businessId]=Business(**args)
        return jsonify(Businesses[businessId]), 201


businesses_api = Blueprint('resources.businesses', __name__)

api = Api(businesses_api)

api.add_resource(Business, '/businesses/<int:businessId>' )

api.add_resource(BusinessList, '/businesses')
