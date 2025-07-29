# pertemuan_12_http_request.py
import requests

url = 'https://httpbin.org/get'
response = requests.get(url)
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
