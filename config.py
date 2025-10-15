import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# API Config
API_KEY = os.getenv('GROQ_API_KEY')

# Project Paths
PROJECT_ROOT = Path(__file__).parent
DOCS_PATH = PROJECT_ROOT/"docs"
