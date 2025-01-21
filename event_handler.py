import sys
import subprocess
import logging
from threading import Timer
from watchdog.events import FileSystemEventHandler

class CustomEventHandler(FileSystemEventHandler):
    def __init__(self):
        self.debounce_timer = None

    def on_created(self, event):
        self.debounce_run_analytics()

    def on_modified(self, event):
        self.debounce_run_analytics()

    def debounce_run_analytics(self):
        if self.debounce_timer:
            self.debounce_timer.cancel()
        self.debounce_timer = Timer(5.0, self.run_analytics)
        self.debounce_timer.start()

    def run_analytics(self):
        logging.info("Running analytics...")
        subprocess.run([sys.executable, "analytics.py"])
