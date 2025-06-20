```python
import socket
from typing import Optional

class ConnectionManager:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.connection = None

    def create_connection(self) -> Optional[socket.socket]:
        try:
            self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.connection.connect((self.host, self.port))
            print(f"Connection established with {self.host} on port {self.port}")
            return self.connection
        except socket.error as e:
            print(f"Network error: {e}")
            return None

    def send_data(self, data: str) -> None:
        try:
            self.connection.sendall(data.encode())
            print(f"Data sent: {data}")
        except socket.error as e:
            print(f"Error sending data: {e}")

    def close_connection(self) -> None:
        try:
            self.connection.shutdown(socket.SHUT_RDWR)  # Shutdown the connection
            self.connection.close()
            print("Connection closed.")
        except socket.error as e:
            print(f"Error closing connection: {e}")

def main() -> None:
    host = 'localhost'
    port = 8080
    connection_manager = ConnectionManager(host, port)
    connection = connection_manager.create_connection()
    
    if connection:
        connection_manager.send_data("Hello, Server!")
        connection_manager.close_connection()

if __name__ == "__main__":
    main()
```