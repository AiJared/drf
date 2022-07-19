import requests

endpoint = "http://127.0.0.1:8000/api/products/19034940393/"

get_response = requests.get(endpoint)
print(get_response.json())