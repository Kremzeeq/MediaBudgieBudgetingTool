from src.common.database import Database
from src.common.utils import Utils
from src.models.users.user_controller import User

Database.initialize()

new_user = True
#Return all documents in dictionary where new_user == True
users_to_authenticate = User.find_new_accounts_to_auth(new_user=new_user)

for user in users_to_authenticate:
    auth_code = Utils.generate_auth_code()
    user.send_auth_email_if_new_user(auth_code)
    user.password =Utils.hash_password(auth_code)
    user.update_user_in_db()







