import jwt

SECRET_KEY = "mysecretkey"

def validate_token(token):
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        print(f"Valid Token: {decoded_token}")
    except jwt.ExpiredSignatureError:
        print("Token has expired.")
    except jwt.InvalidTokenError:
        print("Invalid Token.")

# Sample token
sample_token = jwt.encode({"user": "example"}, SECRET_KEY, algorithm="HS256")
validate_token(sample_token)
