# legacy_file_handler.py

def read_file(file_path):
    try:
        file = open(file_path, 'r')
        content = file.read()
        print content  # Old-style print statement without parentheses
        file.close()
    except IOError, e:
        print "File error:", e

def write_file(file_path, data):
    try:
        file = open(file_path, 'w')
        file.write(data)
        print "Data written to %s" % file_path
        file.close()
    except IOError, e:
        print "File write error:", e

def main():
    file_path = 'sample_file.txt'
    data = "This is some legacy data written to the file.\nMore data follows!"
    
    write_file(file_path, data)
    read_file(file_path)

if __name__ == "__main__":
    main()
