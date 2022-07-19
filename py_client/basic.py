import requests

#endpoint = "https://httpbin.org/status/200/"
#endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"
get_response = requests.post(endpoint, json={"title": "ABC1234", "content": "Hello World", 
"price": 123}) # HTTP Request
# print(get_response.headers)
# print(get_response.text) # print raw text response
# print(get_response.status_code)

# HTTP Request -> HTML
# REST API Request -> JSON
# JSON in full is Javascript Object Notation which is similar with python dict but not exaclty the same
print(get_response.json())