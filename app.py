from flask import Flask
from resources.reviews import reviews_api
from resources.businesses import businesses_api
from resources.users import auth_api

app = Flask(__name__)

app.register_blueprint(businesses_api, url_prefix='/api/v1')
app.register_blueprint(reviews_api, url_prefix='/api/v1')
app.register_blueprint(auth_api, url_prefix='/api/v1/auth')


if __name__ == '__main__':
    app.run(debug=True)
