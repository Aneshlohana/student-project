import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Extract configuration values
APP_NAME = os.getenv("APP_NAME", "Default App")
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
MAX_STUDENTS = int(os.getenv("MAX_STUDENTS", "50"))
