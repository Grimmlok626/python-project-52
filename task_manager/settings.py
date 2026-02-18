import os
import dj_database_url
from dotenv import load_dotenv

load_dotenv()

DATABASES = {
    "default": dj_database_url.config(default=os.getenv("DATABASE_URL"))
}