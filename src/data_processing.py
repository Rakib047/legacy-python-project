def process_data(user_data: list[str]) -> list[str]:
    try:
        processed_data = [item.upper() for item in user_data]
        result = sum(len(item) for item in processed_data)
        print(f"Total length of processed data: {result}")
        return processed_data
    except Exception as e:
        print(f"Error in processing data: {e}")