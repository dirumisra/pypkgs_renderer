from fileinput import filename
import os
from pathlib import Path
import logging

from numpy import true_divide

logging.basicConfig(  
    level=logging.INFO,
    format= "[%(asctime)s : %(levelname)s]: %(message)s")

while True:
    project_name = input("Enter the Project Name:")
    if project_name != "":
        break
    
logging.info(f"Creating Project by Name :{project_name}")

# list of file:

list_of_file = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    "init-setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini"
    ]

for filepath in list_of_file:
    filepath = Path(filepath)
    filedir, filename =  os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir,exist_ok= True)
        logging.info(f"Creating a Directory at :{filedir} for file: {filename}")
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating a New File:{filename} at path:{filepath}")
    else:
        logging.info(f"File is already present at: {filepath}")