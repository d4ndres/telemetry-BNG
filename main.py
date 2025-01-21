import sys
import time
import subprocess
import os
from threading import Timer

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging

class CustomEventHandler(FileSystemEventHandler):
    def __init__(self):
        self.debounce_timer = None

    def on_created(self, event):
        # logging.info(f"Created: {event.src_path}")
        self.debounce_run_analytics()

    def on_modified(self, event):
        # logging.info(f"Modified: {event.src_path}")
        self.debounce_run_analytics()

    def debounce_run_analytics(self):
        if self.debounce_timer:
            self.debounce_timer.cancel()
        self.debounce_timer = Timer(5.0, self.run_analytics)
        self.debounce_timer.start()

    def run_analytics(self):
        logging.info("Running analytics...")
        subprocess.run([sys.executable, "analytics.py"])

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # Directory or file to be monitored
    path = sys.argv[1] if len(sys.argv) > 1 else "..\\VSL"
    
    # Wait until the directory exists
    while not os.path.exists(path):
        logging.info(f"Waiting for directory {path} to be created...")
        time.sleep(5)
    
    # Event handler
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