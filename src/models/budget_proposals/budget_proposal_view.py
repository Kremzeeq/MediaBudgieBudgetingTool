import datetime
from werkzeug.utils import redirect
from flask import Blueprint, request, url_for, render_template

from src.models.products.product_controller import Product
from src.models.countries.country_controller import Country
from src.models.local_budgets.local_budget_controller import Local_budget
from src.models.central_budgets.central_budget_controller import Central_budget
from src.models.budget_proposals.budget_proposal_controller import Budget_proposal
from src.models.product_budget_proposals.product_budget_proposal_controller import Product_budget_proposal

budget_proposal_blueprint = Blueprint('budget_proposal', __name__)

@budget_proposal_blueprint.route('/create_central_proposal_step_1/<string:central_budget_id>',methods=['GET','POST'])
def create_central_proposal_step_1(central_budget_id):
    central_budget = Central_budget.find_by_id(central_budget_id)
    products = [Product.find_product_by_id(product_id)[0] for product_id in central_budget.active_products]
    countries = [Country.find_country_by_id(country_id)[0] for country_id in central_budget.active_countries]
    if request.method == 'POST':
        budget_proposal = Budget_proposal(1)
        for country in countries:
            local_budget = Local_budget(country_id=country._id,budget_proposal_id=budget_proposal._id, status="local_market_to_update")
            local_budget.save_to_db()
            product_budget_proposals = []
            for product in products:
                product_budget_proposal = Product_budget_proposal(product._id)
                product_id_country_id_code = str("product_id_") + str(product._id) + str("_country_id_") + str(country._id)
                product_budget_proposal.country_id = country._id
                product_budget_proposal.product_id = product._id
                product_budget_proposal.central_budget_proposal = request.form.get(product_id_country_id_code)
                product_budget_proposal.local_budget_proposal = None
                new_dict = product_budget_proposal.json()
                product_budget_proposals.append(new_dict)
            budget_proposal.product_budget_proposals = product_budget_proposals
        budget_proposal.save_to_db()
        central_budget.date_updated = datetime.datetime.utcnow()
        central_budget.status = "Central Budget proposed for countries and products"
        central_budget.save_to_db()
        return redirect(url_for('central_budget.show_active'))
    return render_template('budget_proposal/create_central_proposal_step_1.html',
                           central_budget=central_budget, countries=countries, products=products)


