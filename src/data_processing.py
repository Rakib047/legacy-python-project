# src/data_processing.py

# Function to simulate data processing
def process_data(user_data):
    processed_data = []
    try:
        for item in user_data:
            # Simulating a complex processing task
            processed_item = item.upper()  # Simulating some transformation
            processed_data.append(processed_item)
        
        # Simulating a large computation
        result = sum([len(item) for item in processed_data])
        print "Total length of processed data:", result
    except Exception, e:
        print "Error in processing data:", e
    return processed_data
