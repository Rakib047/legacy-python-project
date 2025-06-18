# src/main.py

import sys
from src.utils.helpers import greet_user
from src.db_interaction import fetch_user_data
from src.data_processing import process_data
from src.io_operations import read_file

# Python 2.x style print statements
print "Welcome to the Legacy Python 2.x Codebase!"

def main():
    greet_user("John")  # Greet user with legacy-style greeting

    # Fetching user data from a database (mocked in this case)
    user_data = fetch_user_data("john_doe")

    if user_data:
        print "User data fetched successfully."
        processed_data = process_data(user_data)
        print "Processed data:", processed_data
    else:
        print "No user data found."

    # File operations
    read_file("example_file.txt")

if __name__ == "__main__":
    main()
