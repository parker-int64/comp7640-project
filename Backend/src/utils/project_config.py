from pathlib import Path

BACKEND_DIR = Path(__file__).parent.parent
PROJECT_DIR =  BACKEND_DIR.parent.parent
FRONTEND_DIR = PROJECT_DIR/"Frontend"
STATIC_DIR = FRONTEND_DIR/"dist"
