# Media Budgie: Budgeting Application

**Media Budgie** is a media budgeting python tool, structured as a Flask and REST API application.
Jinja2 coding is applied within html to serve data from a Mongo DB database to the front end-user, who can set up and manage budgets.

<h1 align="center">
  <img src="https://github.com/Kremzeeq/MediaBudgieBudgetingTool/blob/master/src/static/img/Media_Budgie_Logo.jpg" alt="Media Budgie Logo" />
</h1>

## Features

- This early prototype allows a business user to firstly set up a central budget for a budgetary year. 
- They can then proceed to select various countries and products to which the central budget may be distributed.
- Once these pre-sets are established, the business user may proceed to create a central budget proposal for the countries and products.

A later version will provide an alternative user experience in which business users operating within a country can provide a counter local budget proposal for products within their market.

## Prototype Demo

- A prototype of the application simulating a business user journey for setting up central budgets for a business is available here:
https://github.com/Kremzeeq/MediaBudgieBudgetingTool/blob/master/MediaBudgiePrototype.pdf
 
## Project Programming Tools
 
 <h2 align="center">
  <img src="https://github.com/Kremzeeq/MediaBudgieBudgetingTool/blob/master/src/static/img/media_budgie_wordcloud.png" alt="Media Budgie Wordcloud" />
 </h2>

## Project Set-Up

- Module pre-requisites are found in the <a href="https://github.com/Kremzeeq/MediaBudgieBudgetingTool/blob/master/requirements.txt">requirements.txt</a> file
- Opening the project in PyCharm should prompt for modules from the file to be installed
- Alternatively use **pip install** for requirements.txt in the command line

## Changes required in Python Code

| Location                           | Guidance                                                                                       |
|:-----------------------------------|:-----------------------------------------------------------------------------------------------|
| src/config.py                      | Substitute ADMINS frozenset email with a preferred email                                       |
| src/run.py                         | Type a port number as per preferences                                                          |
| src/models/users/user_constants.py | Substitute variables for URL, AUTH_URL, API_KEY, FROM which can be obtained via Mailgun: https://www.mailgun.com/           |
| src/common.database.py             | Database URI is defaulted to "mongodb://127.0.0.1:27017" for your local machine. Please ammend according to preferences.           |
| src/init_DB_collection_presets.py  | Substitute youremail@youremail.com with a preferred email you have access to. Please note this will be authenticated. Please see **Email Authenication** for setting up a password for the front-end application   |

## MongoDB Database Set-Up

- Mongo DB Community Edition 4.0 was installed for this project
- Manual for installing MongoDB on Linux, macOS and Windows is available here:
https://docs.mongodb.com/manual/administration/install-community/

## Initialising Sample data in MongoDB

- Once MongoDB has been configured to preferences, ensure **mongod**, the MongoDB daemon, has been typed into the command line.
- Python script in the following location may then be run: src/init_DB_collection_presets.py
- This will populate the MongoDB MediaBudgie database with data for the user, currency, country and product collections.
- These collections are prerequisites for running the Media Budgie run.py file which enables access to the front-end application
- Please note the pre-sets file can be changed according to preferences
- e.g. at the moment the pre-sets only place focus on European countries and country choices may be expanded

## Email Authentication

- Once a preferred email has been set up in the MongoDB database, run the following python script: src\send_authentication_email.py
- This will prompt for an authentication email to be sent to the email account with an authentication code.
- This will direct the user to an authentication page where the code may be entered
- Thereafter, a password may be set on the registration page
- Logging into the website will redirect to the **Annual Budgeting Portal**
- Please ensure the run.py file is running so the URI can be accessed
- Once registered and during other sessions, all you would need to do is login to view budgeting-related webpages. 

**Copyright: Sian Thompson (Kremzeeq)**

Author Email: sian.thompson@gmx.co.uk
