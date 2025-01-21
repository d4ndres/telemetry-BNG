import sys
import time
import os
import logging
from watchdog.observers import Observer
from event_handler import CustomEventHandler
from utils import wait_for_directory

def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    path = sys.argv[1] if len(sys.argv) > 1 else "..\\VSL"
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