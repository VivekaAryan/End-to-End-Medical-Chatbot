import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


list_of_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    "setup.py",
    "research/test.ipynb",
    "app.py",
    "store_index.py",
    "static/css",
    "templates/index.html"
]

for filepath in list_of_files:
    # Creating a PurePath from string values. 
    # Path automatically rectifies any issues in the string path.
    filepath = Path(filepath)

    # Convering path to Operating System type
    filedir, filename = os.path.split(filepath)

    # Creating the folders and files
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists.")