
from src.common.database import Database
from src.models.products import constants as ProductConstants

class Product(object):
    def __init__(self, product_name, active=False, _id=None):
        self.product_name = product_name
        self.active = active
        self._id = _id if _id is not None else _id

    def insert_product_in_db(self):
        Database.insert(ProductConstants.COLLECTION,self.json())

    def json(self):
        return {
            "_id": self._id,
            "product_name": self.product_name,
            "active":self.active
        }

    @classmethod
    def find_product_docs_in_db(cls):
        return [cls(**elem) for elem in Database.find(ProductConstants.COLLECTION, {})]

    @classmethod
    def find_product_by_id(cls,product_id):
        return [cls(**elem) for elem in Database.find(ProductConstants.COLLECTION, {"_id": product_id})]

    def json_for_central_budget(self):
        return {
            "_id": self._id,
            "active":self.active
        }
    @classmethod
    def find_product_names_by_id(cls,product_ids):
        product_list = []
        for product_id in product_ids:
            product_doc = Database.find_one(ProductConstants.COLLECTION, {"_id": product_id})
            product_list.append(product_doc['product_name'])
        return product_list
