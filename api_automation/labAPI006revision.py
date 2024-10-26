import requests
id=3252
url="https://restful-booker.herokuapp.com/booking/"
full_url=url+str(id)
response_body=requests.get(full_url)
print(response_body.text)
print(response_body.status_code)