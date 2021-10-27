import jwt 
from flask import Flask
import bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask import request
import datetime
from flask import timedelta
from flask import jsonify
from flask import make_response




app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:5432@localhost/python'

db = SQLAlchemy(app)



class User(db.Model):
    #Create a table with database
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    token = db.Column(db.String(500), unique=True, nullable=False)

    def __init__(self, login, password, token=False):
        self.login = login
        self.password = bcrypt.generate_password_hash(
            password, app.config.get('BCRYPT_LOG_ROUNDS')
        ).decode()
        self.token = token


    def encode_auth_token(self, user_id):
        
        try:
           
            return jwt.encode(
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e


    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
            is_users = User.check_blacklist(auth_token)
            if is_users:
                return 'Token blacklisted. Please log in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
    @staticmethod
    def check_blacklist(auth_token):
        # check whether auth token has been blacklisted
        res = User.query.filter_by(token=str(auth_token)).first()
        if res:
            return True
        else:
            return False


    def __repr__(self):
        return '<id: token: {}'.format(self.token)


@app.route('/login')
def login():

    auth = request.authorization

    if auth and auth.password == 'password':
        token = jwt.encode({'user':auth.username, 'exp':datetime.utcnow() + timedelta(minutes=30)}, app.config['SECRET_KEY'])
    
        return jsonify({'token': token.decode('UTF-8')})
    
    return make_response('token value', 401, {'WWW-Authenticate': 'Basic realm="Login required'})

@app.route('/protected')

def protection():
    token = request.args.get('token')
    return '''<h1> The token is {} <h1>'''.format(token)

if __name__ == '__main__':
    app.run(debug=True)
