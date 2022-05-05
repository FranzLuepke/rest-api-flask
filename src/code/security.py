from user import User
import hmac
str_to_bytes = lambda s: s.encode("utf-8") if isinstance(s, str) else s
safe_str_cmp = lambda a, b: hmac.compare_digest(str_to_bytes(a), str_to_bytes(b))

users = [
    User(1, 'Franz', '123456')
]
usernameMapping = {u.username: u for u in users}
userIdMappping = {u.id: u for u in users}

def authenticate(username, password):
    print(username)
    print(password)
    user = usernameMapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    userId = payload['identity']
    return userIdMappping.get(userId, None)