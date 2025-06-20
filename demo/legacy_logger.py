```python
from datetime import datetime

def main():
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Starting the legacy Python 2.x logger.")
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - This is a log entry.")
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Another log entry.")

if __name__ == "__main__":
    main()
```