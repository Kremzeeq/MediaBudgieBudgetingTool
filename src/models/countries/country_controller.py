import uuid
from src.common.database import Database
from src.models.countries import constants as CountryConstants

class Country(object):
    def __init__(self, country_name, currency_id, active=False, _id=None):
        self.country_name = country_name
        self.currency_id = currency_id
        self._id = uuid.uuid4().hex if _id is None else _id
        self.active = active

    def insert_country_in_db(self):
        Database.insert(CountryConstants.COLLECTION,self.json())

    @classmethod
    def find_country_docs_in_db(cls):
        return [cls(**elem) for elem in Database.find(CountryConstants.COLLECTION, {})]

    @classmethod
    def find_country_by_id(cls, country_id):
        return [cls(**elem) for elem in Database.find(CountryConstants.COLLECTION, {"_id": country_id})]

    def json_for_central_budget(self):
        return {
            "_id": self._id,
            "active":self.active
        }

    @classmethod
    def find_country_names_by_id(cls,country_ids):
        country_list = []
        for country_id in country_ids:
            country_doc = Database.find_one(CountryConstants.COLLECTION, {"_id": country_id})
            country_list.append(country_doc['country_name'])
        return country_list

    def json(self):
        return {
            "_id" :self._id,
            "country_name" : self.country_name,
            "currency_id" : self.currency_id,
            "active" : self.active
        }
