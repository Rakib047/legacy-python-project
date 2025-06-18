# src/io_operations.py

def read_file(file_path):
    try:
        # Simulating file reading in Python 2.x (old-style)
        file = open(file_path, 'r')
        content = file.read()
        print content  # No parentheses in print
        file.close()
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
