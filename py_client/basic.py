import requests

# endpoint = "https://httpbin.org/status/200"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_request = requests.get(endpoint, json={"query": "Hello World"})
print(get_request.headers)
print(get_request.text)
# print(get_request.status_code)
# print(get_request.text)
# print(get_request.json())