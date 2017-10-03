import sys
import time
import logging
import subprocess
import os
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

processes = set()

class MyEventHandler(LoggingEventHandler):
    def on_modified(self, event):
        super(LoggingEventHandler, self).on_modified(event)
        if len(processes) != 0:
            os.system('pkill -9 python')
        processes.add(subprocess.Popen(['python','main.py']))
        # subprocess.check_output(['pkill',' -f main.py'])
        what = 'directory' if event.is_directory else 'file'
        logging.info("Modified %s: %s", what, event.src_path)

if __name__ == "__main__":
    processes.add(subprocess.Popen(['python','main.py']))
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = MyEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()