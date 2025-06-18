# legacy_logger.py

import time

def log(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open("legacy_log.txt", "a") as log_file:
        log_file.write("[%s] %s\n" % (timestamp, message))

def main():
    log("Starting the legacy Python 2.x logger.")
    log("This is a log entry.")
    log("Another log entry.")

if __name__ == "__main__":
    main()
