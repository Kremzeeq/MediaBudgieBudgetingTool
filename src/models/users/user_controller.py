import uuid
import requests
import datetime

from src.common.utils import Utils
from src.common.database import Database
import src.models.users.user_errors as UserErrors
import src.models.users.user_constants as UserConstants

class User(object):

    def __init__(self, email, password=None, user_role = "system_admin", new_user = True, active= False,_id=None, date_authenticated=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.email = email
        self.password = Utils.hash_password(Utils.generate_auth_code()) if password is None else password
        self.user_role = user_role
        self.new_user = new_user
        self.active = active
        self.date_authenticated = datetime.datetime.utcnow() if date_authenticated is None else date_authenticated

    @classmethod
    def find_new_accounts_to_auth(cls, new_user):
        return [cls(**user_doc) for user_doc in Database.find(UserConstants.COLLECTION, {'new_user': new_user})]

    def send_auth_email_if_new_user(self, auth_code):
        return requests.post(UserConstants.URL,
            auth =("api",UserConstants.API_KEY),
            data={
                "from": UserConstants.FROM,
                "to": self.email,
                "subject":"Media Budgie: Authorisation Message",
                "text": 'Welcome to Media Budgie! \n\n'
                        'Media Budgie is a Media Budgeting Tool which can help you with '
                        'annual and monthly budgeting\n\n'
                        'Please click here visit ({}) and enter your authorisation code on the registration page: \n\n'
                        '{}'.format(UserConstants.AUTH_URL,auth_code)
                })

    @staticmethod
    def authenticate_user(email, password):
        user_data = Database.find_one(UserConstants.COLLECTION, {"email": email})
        if user_data is None:
            raise UserErrors.UserDoesNotExistError("Your user account does not exist")
        if not Utils.check_hashed_password(password, user_data['password']):
            raise UserErrors.IncorrectAuthCodeCode("Your authentication code was incorrect")
        return True

    @staticmethod
    def register_user(email, password):
        # need further password check for security on user['password']
        user_data = Database.find_one(UserConstants.COLLECTION, {"email": email})
        if Utils.check_hashed_password(password, user_data['password']):
            raise UserErrors.PoorPasswordError("Please ensure to enter a secure password")
        user_data =User(email,password, _id=user_data['_id'])
        user_data.new_user = False
        user_data.active = True
        user_data.password = Utils.hash_password(password)
        user_data.update_user_in_db()
        return True

    def insert_user_in_db(self):
        Database.insert(UserConstants.COLLECTION,self.json())

    def update_user_in_db(self):
        Database.update(UserConstants.COLLECTION,{"_id": self._id}, self.json())

    def json(self):
        return {
            "_id": self._id,
            "email": self.email,
            "password": self.password,
            "user_role": self.user_role,
            "new_user": self.new_user,
            "active": self.active,
            "date_authenticated": self.date_authenticated
        }

    @staticmethod
    def find_email_from_DB(self,email):
        # check if email is in database
        if Database.find_one(UserConstants.COLLECTION,{"email":email}):
            return True

    @classmethod
    def find_user_object_from_DB(cls,email):
        return cls(**Database.find_one(UserConstants.COLLECTION,{"email":email}))

    @staticmethod
    def validate_user_login(email, password):
        user_data = Database.find_one(UserConstants.COLLECTION, {"email": email})
        if user_data is None:
            raise UserErrors.UserDoesNotExistError("Your user account does not exist")
        if not Utils.check_hashed_password(password, user_data['password']):
            raise UserErrors.IncorrectPasswordError("Your password was incorrect")
        return True

