from flask import Flask, render_template
from src.common.database import Database

app = Flask(__name__, template_folder="templates")
app.config.from_object('config')
app.secret_key = '123'

@app.before_first_request
def init_db():
    Database.initialize()

@app.route('/')
def home():
    return render_template('home.html')

from src.models.users.user_view import user_blueprint
from src.models.central_budgets.central_budget_view import central_budget_blueprint
from src.models.budget_proposals.budget_proposal_view import budget_proposal_blueprint

app.register_blueprint(user_blueprint, url_prefix="/users")
app.register_blueprint(central_budget_blueprint, url_prefix="/central_budget")
app.register_blueprint(budget_proposal_blueprint, url_prefix="/budget_proposal")

