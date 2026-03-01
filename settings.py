import os
from dotenv import load_dotenv

def get_default_env_path() -> str:
    return os.path.join(os.path.dirname(__file__), '.env')

def build_settings():
    load_dotenv(get_default_env_path())
    # לדוגמה, אפשר להחזיר הגדרות שקשורות לאימיילים או לשירותים אחרים
    return {
        "email_service": {
            "smtp_host": os.getenv("SMTP_HOST"),
            "smtp_port": os.getenv("SMTP_PORT")
        }
    }
