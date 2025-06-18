def fetch_user_data(username: str) -> list[str] | None:
    if username == "john_doe":
        return ["John", "Doe", "john.doe@example.com"]
    raise ValueError("User not found")