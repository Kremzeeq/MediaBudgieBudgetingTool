import uuid

class Product_budget_proposal(object):
    def __init__(self, budget_proposal_id, country_id=None, product_id=None,
                 central_budget_proposal=None, local_budget_proposal=None, _id=None):
        self.budget_proposal_id = budget_proposal_id,
        self.country_id = country_id
        self.product_id = product_id
        self.central_budget_proposal = central_budget_proposal
        self.local_budget_proposal = local_budget_proposal
        self._id = uuid.uuid4().hex if _id is None else _id

    def json(self):
        return{
            "_id": self._id,
            "budget_proposal_id": self.budget_proposal_id,
            "country_id": self.country_id,
            "product_id": self.product_id,
            "central_budget_proposal": self.central_budget_proposal,
            "local_budget_proposal": self.local_budget_proposal
             }