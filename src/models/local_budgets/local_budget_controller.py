import uuid
from src.common.database import Database
import src.models.local_budgets.constants as LocalBudgetConstants

class Local_budget(object):
    def __init__(self, country_id, budget_proposal_id, status="active", _id=None):
        self.country_id = country_id,
        self.budget_proposal_id = budget_proposal_id
        self.status = status
        self._id = uuid.uuid4().hex if _id is None else _id

    def save_to_db(self):
        Database.insert(LocalBudgetConstants.COLLECTION, self.json())

    def json(self):
        return {
            "_id": self._id,
            "country_id":self.country_id,
            "budget_proposal_id": self.budget_proposal_id,
            "status": self.status
         }



