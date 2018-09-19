import uuid
from src.common.database import Database
import src.models.budget_proposals.constants as BudgetProposalConstants

class Budget_proposal(object):
    def __init__(self, version, product_budget_proposals=None, _id=None):
        self.version = version
        self.product_budget_proposals = product_budget_proposals
        self._id = uuid.uuid4().hex if _id is None else _id

    def save_to_db(self):
        return Database.insert(BudgetProposalConstants.COLLECTION,self.json())

    def json(self):
        return{
            "_id": self._id,
         "version": self.version,
         "product_budget_proposals": self.product_budget_proposals
         }

