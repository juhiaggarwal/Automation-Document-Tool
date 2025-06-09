import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Flask Config
    SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key")

    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///site.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Email Configuration (Gmail SMTP)
    EMAIL_USER = os.getenv("EMAIL_USER")
    EMAIL_PASS = os.getenv("EMAIL_PASS")
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587  # TLS

    # OpenAI Configuration
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    # Google OAuth
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")

     # GitHub OAuth
    GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
    GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
    
    # Aspose credentials
 
    ASPOSE_CLIENT_ID = os.getenv("ASPOSE_CLIENT_ID")
    ASPOSE_CLIENT_SECRET = os.getenv("ASPOSE_CLIENT_SECRET")
    