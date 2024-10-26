import requests
response_body=requests.get("https://restful-booker.herokuapp.com/booking/461")
print(response_body.text)
print(response_body.headers)