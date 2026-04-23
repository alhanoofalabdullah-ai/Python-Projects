
## main.py

```python
import csv

input_file = "raw_data.csv"
output_file = "cleaned_data.csv"


def clean_value(value):
    return value.strip().lower()


def clean_data():
    cleaned_rows = []

    try:
        with open(input_file, "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                if not row or all(cell.strip() == "" for cell in row):
                    continue

                cleaned_row = [clean_value(cell) for cell in row]
                cleaned_rows.append(cleaned_row)

        with open(output_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(cleaned_rows)

        print("Data cleaned successfully.")
        print(f"Cleaned file saved as: {output_file}")

    except FileNotFoundError:
        print("Input file not found.")


if __name__ == "__main__":
    clean_data()
