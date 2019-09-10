import logging
from watchdog.events import LoggingEventHandler

# Enter your path here
PATH = "/app/"  # Example "C:\\your_path\\"

# Enter time format you want to display

TIMEFORMAT = '%Y-%m-%d %H:%M:%S' #Default '%Y-%m-%d %H:%M:%S'

# Select the type of events you want to display
MOVED_FILES_OR_FOLDERS = True
MODIFIED_FILES_OR_FOLDERS = True
CREATED_FILES_OR_FOLDERS = True
DELETED_FILES_OR_FOLDERS = True


# Event handler
class EventHandler(LoggingEventHandler):
    def on_moved(self, event):
        if MOVED_FILES_OR_FOLDERS:
            logging.info(f"Moved from '{event.src_path}' to '{event.dest_path}'")
    def on_created(self, event):
        if CREATED_FILES_OR_FOLDERS:
            logging.info(f"Created '{event.src_path}'")
    def on_deleted(self, event):
        if DELETED_FILES_OR_FOLDERS:
            logging.info(f"Deleted '{event.src_path}'")
    def on_modified(self, event):
        if MODIFIED_FILES_OR_FOLDERS:
            logging.info(f"Modified '{event.src_path}'")
