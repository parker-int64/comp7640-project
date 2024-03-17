import os
import logging
import subprocess
from Backend.src.utils.project_config import (BACKEND_DIR, PROJECT_DIR, FRONTEND_DIR)

def env_check():
    """
        check the environments
    """

def check_if_rebuild() -> bool:
    """
        check wether to rebuild the frontend files
    """
    return False

def build_frontend():
    """
        It will build the frontend files
    """

    logging.info("Building the frontend files...")
    process = subprocess.Popen([
        "npm", "run", "build"
    ], cwd=FRONTEND_DIR, shell=True)
    process.wait()


def main():
    """
        running the Flask app 
    """

    build_frontend()

    process = subprocess.Popen([
        "python", "app.py"
    ], cwd=BACKEND_DIR, shell=True)

    logging.info("Launching the program...")

    process.wait()



if __name__ == "__main__":
    main()
    