import sys
import time
import os
import logging
from watchdog.observers import Observer
from event_handler import CustomEventHandler
from utils import wait_for_directory
from dotenv import load_dotenv
from gui import TelemetryGUI
import tkinter as tk

class TelemetryApp:
    def __init__(self):
        self.observer = None

    def start_monitoring(self):
        load_dotenv()  # Load environment variables from .env file
        path = os.getenv("VSL_PATH")

        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')

        wait_for_directory(path)

        event_handler = CustomEventHandler()
        self.observer = Observer()
        self.observer.schedule(event_handler, path, recursive=True)
        self.observer.start()

    def stop_monitoring(self):
        if self.observer:
            self.observer.stop()
            self.observer.join()
            self.observer = None

def main():
    app = TelemetryApp()
    
    root = tk.Tk()
    gui = TelemetryGUI(root, app)
    root.mainloop()

if __name__ == "__main__":
    main()