import os
import sys
import logging
import subprocess
import platform
from pathlib import Path
from Backend.src.utils.project_config import (BACKEND_DIR, FRONTEND_DIR)


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

logger = logging.getLogger(__name__)


CURRENT_PLATFORM = platform.system()

def env_check() -> bool:
    """
        check the environments
    """
    try:
        logging.info("Current platform %s", CURRENT_PLATFORM)

         # we can directly output the python version, 'python -V' is unnecessary
        logging.info("Python version %s", sys.version) 
        pip_check = subprocess.run(["pip", "-V"],capture_output=True, text=True, check=False)
        logging.info("pip version %s", pip_check.stdout.strip())
        node_check = subprocess.run(["node", "-v"], capture_output=True, text=True, check=False)
        logging.info("Node version %s", node_check.stdout.strip())

        # Who the hell know why npm in windows is not a executable file...
        npm_check = subprocess.run(["npm", "-v"],
                                   shell=CURRENT_PLATFORM == "Windows",
                                   capture_output=True, text=True, check=False)

        logging.info("npm version %s", npm_check.stdout.strip())
        
        # Check the sql status, note currently this is a warning level.
        # It shouldn't affect the other part of program.

        # On windows, we support both mysql and mariadb
        if CURRENT_PLATFORM == 'Windows':
            mysql_status = subprocess.run(["sc", "query", "mysql"],
                                          capture_output=True, text=True, check=False)

            mariadb_status = subprocess.run(["sc", "query", "mariadb"],
                                            capture_output=True, text=True, check=False)

            if "RUNNING" in mysql_status.stdout.strip() or "RUNNING" in mariadb_status.stdout.strip():
                logging.info("Found running services of MySQL or MariaDB.")
            else:
                logging.warning("No running instance of MySQL or MariaDB were found.\n"
                                "Consider installing or starting the sql services.")

        elif CURRENT_PLATFORM == "Linux":

            mysql_status = subprocess.run(['systemctl', 'is-active', 'mysql'],
                                          capture_output=True, text=True, check=False)

            mariadb_status = subprocess.run(['systemctl', 'is-active', 'mariadb'],
                                            capture_output=True, text=True, check=False)

            if mysql_status.stdout.strip() == "active" or mariadb_status.stdout.strip() == "active":
                logging.info("Found running services of MySQL or MariaDB.")
            else:
                logging.warning("No running instance of MySQL or MariaDB were found.\n"
                                "Consider installing or starting the sql services.")       


        # So, mariadb in Apple Silicon is distributed with source code.
        # It seems oracle have a binary distribution, therefore we only choose mysql on mac.
        # Also, normally you cannot determine if the service is running though 'mysql.server status'
        # since only root user can use that command.
        elif CURRENT_PLATFORM == "Darwin":

            mysql_status = subprocess.run(["pgrep", "mysqld"],
                                          capture_output=True, text=True, check=False)

            if len(mysql_status.stdout.strip()) != 0:
                logging.info("Found running services of MySQL, PID %s", mysql_status.stdout.strip())
            else:
                logging.warning("No running instance of MySQL were found.\n"
                                "Consider installing or starting the sql services.")
        else:
            logging.info("Unsupported platform")
            sys.exit(-1)



    except subprocess.CalledProcessError as e:
        logging.error("Some of the requirements were not satisfied: \n %s", e.output)
        return False
    except FileNotFoundError:
        logging.error("Script or executable not found")
        return False

    return True

def check_if_rebuild() -> bool:
    """
        check wether to rebuild the frontend files
        so this is a simple check if we have the 'index.html'
        in the designate directory.

        if not, we should rebuild the vue project.
    """
    if not Path(FRONTEND_DIR/"dist"/"index.html").exists():
        logging.info("No dist directory were found. Building the frontend...")
        return True
    logging.info("Found maybe existing build files, skip the build process.")
    return False

def build_frontend():
    """
        It will build the frontend files
    """
    logging.info("Building the frontend files...")

    try:
        with subprocess.Popen([
            "npm", "install"
        ], cwd=FRONTEND_DIR, shell= CURRENT_PLATFORM == "Windows") as p:
            p.wait()
        # if we have the 'dist' directory, usually dont need to rebuild
        # this should save some time.
        if check_if_rebuild():
            with subprocess.Popen([
                "npm", "run", "build"
            ], cwd=FRONTEND_DIR, shell= CURRENT_PLATFORM == "Windows") as p1:
                p1.wait()
    except subprocess.CalledProcessError as e:
        logging.error("Error building the frontend... \n %s", e.output)
        logging.info("Consider running 'npm install' and 'npm run build' in frontend directory.")


def main():
    """
        running the Flask app 
    """

    # comment the following statement to disable the debug mode
    os.environ["FLASK_DEBUG"] = "True"

    if env_check():

        build_frontend()

        logging.info("Launching the program...")

        try:
            with subprocess.Popen([
                sys.executable, "app.py"
            ], cwd=BACKEND_DIR) as flask_app:
                flask_app.wait()

        except subprocess.CalledProcessError as e:
            logging.error("Unable to launch program: \n%s", e.output)

if __name__ == "__main__":
    main()
    