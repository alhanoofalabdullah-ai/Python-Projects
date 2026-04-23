import requests

API_URL = "https://jsonplaceholder.typicode.com/users"


def fetch_data():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        users = response.json()

        print("Users List:\n")

        for user in users:
            print(f"Name: {user['name']}")
            print(f"Email: {user['email']}")
            print(f"City: {user['address']['city']}")
            print("-" * 30)

    except requests.exceptions.RequestException as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    fetch_data()
