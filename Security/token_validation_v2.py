import jwt

SECRET_KEY = "newsecretkey"

def validate_token_v2(token):
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        print(f"Valid Token: {decoded_token}")
    except jwt.ExpiredSignatureError:
        print("Token has expired.")
    except jwt.InvalidTokenError:
        print("Invalid Token.")

# Sample token
sample_token_v2 = jwt.encode({"user": "new_example"}, SECRET_KEY, algorithm="HS256")
validate_token_v2(sample_token_v2)
