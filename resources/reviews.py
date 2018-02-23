from flask import Flask, jsonify, Blueprint

from flask_restful import Resource, abort, Api, reqparse
import json 

from models import Review


Reviews = {
    1: Review(1, 2, 'short comment', 5).__dict__,
    2: Review(2, 3, 'short comment', 9).__dict__,
    3: Review(3, 1, 'short comment', 7).__dict__
}


class Review(Resource):
    """
    Just a test to see if I could return all reviews regardless of the  business
    """
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'reviewer_id',
            required=True,
            help='No name provided',
            location=['form', 'json']
        )

    def get(self):
        return jsonify(Reviews)


class ReviewList(Resource):
    """
    List all reviews of a business
    Add a new review to the list of a business
    """

    def get(self, businessId):
        reviews = []
        rkeys = Reviews.keys()
        for rkey in rkeys:
            if Reviews[rkey].business_id == businessId:
                reviews.add(Reviews[rkey])
        return jsonify(reviews) 

    def post(self, reviewId):
        args = reqparse.parse_args()
        reviewId = int(max(Reviews.keys())+1)
        Reviews[reviewId] = Review(**args)
        return jsonify(Reviews[reviewId])


reviews_api = Blueprint('resources.reviews', __name__)

api = Api(reviews_api)

api.add_resource(ReviewList, '/businesses/<int:businessId>/reviews')
api.add_resource(Review, '/businesses/reviews')
