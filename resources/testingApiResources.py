import unittest
from resources import reviews
from resources import businesses
from models import Business, Review, User


class BusinessesTestCase(unittest.TestCase):
    """
    This class tests businesses resources
    """

    def setUp(self):
        self.client = self.app.test_client()
        self.businessList = businesses.Businesses
        self.business = Business('Buz1', 'short description', 1, 'cat1', 'loc1').__dict__


    def test_business_creation(self):
        result = self.client.post('/businesses', data=self.business)
        self.assertEqual(result.status_code, 201)
    

    def test_business_profile_can_be_edited(self):
        result = self.client.put('/businesses/<int:businessId>', data=self.business)
        self.assertEqual(result.status_code, 201)

    def test_business_can_be_deleted(self):
        result = self.client.post('/')

    def test_api_can_retrieve_business_by_id(self):


    def test_api_can_retrieve_all_businesses(self):

    


class ReviewsTestCase(unittest.TestCase):
    """
    This class contains test cases for review resources.
    """

    def test_review_creation(self):

    def test_api_can_retrieve_all_reviews_of_a_business(self):


