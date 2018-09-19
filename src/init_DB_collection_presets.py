from src.common.database import Database
from src.models.users.user_controller import User
from src.models.products.product_controller import Product
from src.models.countries.country_controller import Country
from src.models.currencies.currency_controller import Currency

#Initialize MediaBudgieDB
Database.initialize()

# Set up users in DB
user=User("youremail@youremail.com", user_role="system_admin", new_user=True)
user.insert_user_in_db()

#Set up currencies in DB
currency = Currency(_id= "1",currency_name="English_Pound")
currency.insert_currency_in_db()
currency = Currency(_id= "2",currency_name="Euro")
currency.insert_currency_in_db()

#Set up Countries in DB

country= Country(_id= "1", country_name= "UK", currency_id=1)
country.insert_country_in_db()
country= Country(_id= "2", country_name= "Germany", currency_id=2)
country.insert_country_in_db()
country= Country(_id= "3", country_name= "France", currency_id=2)
country.insert_country_in_db()
country= Country(_id= "4", country_name= "Italy", currency_id=2)
country.insert_country_in_db()
country= Country(_id= "5", country_name= "Spain", currency_id=2)
country.insert_country_in_db()

#Set up Products in DB
product = Product(_id="1", product_name="product_1")
product.insert_product_in_db()
product = Product(_id="2", product_name="product_2")
product.insert_product_in_db()
product = Product(_id="3", product_name="product_3")
product.insert_product_in_db()
product = Product(_id="4", product_name="product_4")
product.insert_product_in_db()
product = Product(_id="5", product_name="product_5")
product.insert_product_in_db()