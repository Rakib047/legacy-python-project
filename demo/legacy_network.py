# legacy_network.py

import socket

def create_connection(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        print "Connection established with %s on port %d" % (host, port)
        return s
    except socket.error, e:
        print "Network error: %s" % e
        return None

def send_data(conn, data):
    try:
        conn.sendall(data)
        print "Data sent: %s" % data
    except socket.error, e:
        print "Error sending data: %s" % e

def close_connection(conn):
    try:
        conn.close()
        print "Connection closed."
    except socket.error, e:
        print "Error closing connection: %s" % e

def main():
    host = 'localhost'
    port = 8080
    connection = create_connection(host, port)
    
    if connection:
        send_data(connection, "Hello, Server!")
        close_connection(connection)

if __name__ == "__main__":
    main()
