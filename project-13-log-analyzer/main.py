
---

## main.py

```python
log_file = "logs.txt"


def analyze_logs():
    try:
        with open(log_file, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Log file not found.")
        return

    error_count = 0
    warning_count = 0
    info_count = 0

    for line in lines:
        if "ERROR" in line:
            error_count += 1
        elif "WARNING" in line:
            warning_count += 1
        elif "INFO" in line:
            info_count += 1

    print("Log Analysis Report")
    print("-------------------")
    print(f"ERROR: {error_count}")
    print(f"WARNING: {warning_count}")
    print(f"INFO: {info_count}")


if __name__ == "__main__":
    analyze_logs()
