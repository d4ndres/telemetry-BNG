import os
import time
import logging

def wait_for_directory(path):
    while not os.path.exists(path):
        logging.info(f"Waiting for directory {path} to be created...")
        time.sleep(5)
