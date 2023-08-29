import auth_token as auth

# for this to work you must have a import auth_token as auth and auth_token.py
#    must have a token = "yourTokenHere" string
auth_token = {"Authorization": "Bearer " + auth.token}
ver = "/v2/"
