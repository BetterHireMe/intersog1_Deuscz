import time
import logging
from watchdog.observers import Observer
from settings import *

if __name__ == "__main__":
    # Logging your events
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt=TIMEFORMAT)
    # Path to your folder
    path = PATH
    event_handler = EventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()