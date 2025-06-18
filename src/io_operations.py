# src/io_operations.py

import os

def read_file(file_path):
    try:
        # Get the absolute path for the file
        file_path = os.path.abspath(file_path)
        # Open and read the file
        with open(file_path, 'r') as file:
            content = file.read()
            print content  # Python 2.x style print
    except IOError, e:
        print "File error:", e

def write_file(file_path, data):
    try:
        # Writing to a file (outdated method)
        with open(file_path, 'w') as file:
            file.write(data)
        print "Data written to", file_path
    except IOError, e:
        print "File write error:", e
