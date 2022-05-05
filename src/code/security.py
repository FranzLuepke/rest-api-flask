from user import User
from werkzeug.security import safe_str_cmp

users = [
    User(1, 'Franz', '123456')
]
userNameMapping = {u.userName for u in users}
userIdMappping = {u.id for u in users}

def authenticate(userName, password):
    user = userNameMapping.get(userName, None)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    userId = payload['identity']
    return userIdMappping.get(userId, None)