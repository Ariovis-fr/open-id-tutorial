import os
from dotenv import load_dotenv

load_dotenv(override=True)

CLIENT_ID = os.getenv("OIDC_CLIENT_ID", "client_id")
CLIENT_SECRET = os.getenv("OIDC_CLIENT_SECRET", "client_secret")
AUTHORITY = os.getenv("OIDC_AUTHORITY", "your_authority")
REDIRECT_URI = os.getenv("REDIRECT_URI", "client_redirect_uri")


class Config:
    PREFERRED_URL_SCHEME = "http"
    PORT = 8081
    SECRET_KEY = os.getenv("SECRET_KEY", "dev")
    SESSION_TYPE = "filesystem"
    SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = 3600  # 1 hour
