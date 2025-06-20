import socket
from typing import Optional

def create_connection(host: str, port: int) -> Optional[socket.socket]:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        print(f"Connection established with {host} on port {port}")
        return s
    except socket.error as e:
        print(f"Network error: {e}")
        return None

def send_data(conn: socket.socket, data: str) -> None:
    try:
        conn.sendall(data.encode())
        print(f"Data sent: {data}")
    except socket.error as e:
        print(f"Error sending data: {e}")

def close_connection(conn: socket.socket) -> None:
    try:
        conn.close()
        print("Connection closed.")
    except socket.error as e:
        print(f"Error closing connection: {e}")

def main() -> None:
    host = 'localhost'
    port = 8080
    connection = create_connection(host, port)
    
    if connection:
        send_data(connection, "Hello, Server!")
        close_connection(connection)

if __name__ == "__main__":
    main()