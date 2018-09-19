from src.common.database import Database
from src.models.currencies import constants as CurrencyConstants

class Currency(object):
    def __init__(self, _id, currency_name):
        self._id = _id
        self.currency_name= currency_name

    def insert_currency_in_db(self):
        Database.insert(CurrencyConstants.COLLECTION,self.json())

    def json(self):
        return {
            "_id": self._id,
            "currency_name": self.currency_name
        }
