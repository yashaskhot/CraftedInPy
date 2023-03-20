import requests

email=input("Enter your email: ")
url = f"https://disposable.debounce.io/?email={email}"



headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)