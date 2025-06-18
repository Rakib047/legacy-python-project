# src/db_interaction.py

# Simulated function to fetch user data
def fetch_user_data(username):
    try:
        # Simulating an old database fetch operation
        # In Python 2.x, this might have been using older DB-API 2.0
        if username == "john_doe":
            return ["John", "Doe", "john.doe@example.com"]  # Simulated user data
        else:
            raise ValueError("User not found")
    except ValueError, e:
        print "Error:", e
        return None
