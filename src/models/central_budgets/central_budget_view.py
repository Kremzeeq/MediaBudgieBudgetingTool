
from flask import Blueprint, request, session, url_for, render_template
from werkzeug.utils import redirect
from src.models.central_budgets.central_budget_controller import Central_budget
from src.models.countries.country_controller import Country
from src.models.products.product_controller import Product

central_budget_blueprint = Blueprint('central_budget', __name__)

@central_budget_blueprint.route('/create_budget_step_1', methods=['GET','POST'])
def create_budget_step_1():
    central_budget = Central_budget()
    if request.method == 'POST':
        central_budget.budget_year = request.form['year']
        central_budget.central_budget_value = request.form['central_budget_value']
        central_budget.save_to_db()
        return redirect(url_for('central_budget.create_budget_step_2', central_budget_id = central_budget._id))
    return render_template('central_budget/create_budget_step_1.html', central_budget=central_budget)

@central_budget_blueprint.route('/create_budget_step_2/<string:central_budget_id>', methods=['GET','POST'])
def create_budget_step_2(central_budget_id):
    central_budget = Central_budget.find_by_id(central_budget_id)
    country_docs = Country.find_country_docs_in_db()
    if request.method == 'POST':
        central_budget.active_countries = request.form.getlist('country_ids')
        central_budget.save_to_db()
        return redirect(url_for('central_budget.create_budget_step_3', central_budget_id = central_budget._id))
    return render_template('central_budget/create_budget_step_2.html', central_budget = central_budget, country_docs=country_docs)

@central_budget_blueprint.route('/create_budget_step_3/<string:central_budget_id>', methods=['GET','POST'])
def create_budget_step_3(central_budget_id):
    central_budget = Central_budget.find_by_id(central_budget_id)
    product_docs = Product.find_product_docs_in_db()
    if request.method == 'POST':
        central_budget.active_products = request.form.getlist('product_ids')
        central_budget.save_to_db()
        return redirect(url_for('central_budget.show_active'))
    return render_template('central_budget/create_budget_step_3.html', central_budget=central_budget, product_docs=product_docs)

@central_budget_blueprint.route('/show_active')
def show_active():
    central_budgets = Central_budget.find_active_docs_in_db()
    return render_template('central_budget/show_active.html', central_budgets=central_budgets)

@central_budget_blueprint.route('/central_budget_page/<string:central_budget_id>')
def central_budget_page(central_budget_id):
    central_budget = Central_budget.find_by_id(central_budget_id)
    temp_countries = Country.find_country_names_by_id(central_budget.active_countries)
    temp_products = Product.find_product_names_by_id(central_budget.active_products)

    return render_template('central_budget/central_budget_page.html',
                           central_budget=central_budget, temp_countries=temp_countries, temp_products=temp_products)



