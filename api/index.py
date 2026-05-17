import sys
from pathlib import Path

# Add project root to python path to allow backend package imports
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# Import the FastAPI application
from backend.app.main import app

# Vercel Serverless requires the application to be exposed as `app`
