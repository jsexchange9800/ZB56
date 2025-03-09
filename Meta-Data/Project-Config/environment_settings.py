import os

ENV_MODE = "development"  # Possible values: development, production

def set_environment():
    if ENV_MODE == "production":
        os.environ['DATABASE_URL'] = 'prod-db-url'
    else:
        os.environ['DATABASE_URL'] = 'dev-db-url'
