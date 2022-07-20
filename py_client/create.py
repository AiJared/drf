from email import header
import requests


headers = {'Authorization': 'Bearer 21cbfb4bad8e3a0103defd552038bbf11f9a6c75'}
endpoint = "http://127.0.0.1:8000/api/products/"
data = {
    'title': "This field is done",
    'price': 32.99
}

get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())