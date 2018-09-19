import uuid
import datetime
from src.common.database import Database
import src.models.central_budgets.constants as CentralBudgetConstants

class Central_budget(object):
    def __init__(self, budget_year=None, central_budget_value=None,active_countries=None,active_products=None,local_budgets=None, exchange_rates=None,date_created=None, date_updated=None, active=True, _id=None, status="Central Budget to be proposed for countries and products"):
        self.budget_year = budget_year
        self.central_budget_value = central_budget_value
        self.active_countries = active_countries
        self.active_products = active_products
        self.local_budgets = local_budgets
        self.exchange_rates = exchange_rates
        self.date_created = datetime.datetime.utcnow() if date_created is None else date_created
        self.date_updated = datetime.datetime.utcnow() if date_updated is None else date_updated
        self.active = active
        self._id = uuid.uuid4().hex if _id is None else _id
        self.status = status

    def init_next_year(self):
        now = datetime.datetime.now()
        this_year = int(now.year)
        next_year = this_year + 1
        return int(next_year)

    @classmethod
    def find_central_budgets_for_budget_year(cls, budget_year):
        return [cls(**elem) for elem in Database.find(CentralBudgetConstants.COLLECTION, {'budget_year': budget_year})]

    def save_to_db(self):
        return Database.update(CentralBudgetConstants.COLLECTION, {"_id": self._id}, self.json())

    def json(self):
        return {
            "_id":self._id,
            "budget_year":self.budget_year,
            "central_budget_value":self.central_budget_value,
            "active_countries": self.active_countries,
            "active_products": self.active_products,
            "local_budgets":self.local_budgets,
            "exchange_rates":self.exchange_rates,
            "date_created": self.date_created,
            "date_updated": self.date_updated,
            "active": self.active,
            "status": self.status
        }

    @classmethod
    def find_active_docs_in_db(cls):
        return [cls(**elem) for elem in Database.find(CentralBudgetConstants.COLLECTION, {"active": True})]

    def activate(self):
        self.active = True
        self.save_to_db()

    def deactivate(self):
        self.active = False
        self.save_to_db()

    @classmethod
    def find_by_id(cls, central_budget_id):
        return cls(**Database.find_one(CentralBudgetConstants.COLLECTION, {'_id': central_budget_id}))
