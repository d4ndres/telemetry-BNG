import sys
import time
import os
import logging
from watchdog.observers import Observer
from event_handler import CustomEventHandler
from utils import wait_for_directory
from dotenv import load_dotenv

def main():
    load_dotenv()  # Load environment variables from .env file

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    path = os.getenv("VSL_PATH")
    wait_for_directory(path)

    event_handler = CustomEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()