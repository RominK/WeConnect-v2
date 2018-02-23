
class User():
    def __init__(self, username, firstname, lastname, email, password, is_auth=False):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.is_auth = is_auth


class Business():
    def __init__(self, name, description, owner_id, category, location):
        self.name = name
        self.owner_id = owner_id
        self.description = description
        self.category = category
        self.location = location


class Review():
    def __init__(self, business_id, reviewer_id, comment, rating):
        self.business_id = business_id
        self.reviewer_id = reviewer_id
        self.comment = comment
        self.rating = rating




