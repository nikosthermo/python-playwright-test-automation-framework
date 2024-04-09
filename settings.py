from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
