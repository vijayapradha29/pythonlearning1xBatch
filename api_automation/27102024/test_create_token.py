import requests
import pytest
from requests.cookies import create_cookie


@pytest.mark.positive
def create_token():
    URL="https://restful-booker.herokuapp.com/auth"
    headers1={"Content-Type":"application/json"}
    json_payload={
    "username" : "admin",
    "password" : "password123"
}
    response1=requests.post(url=URL,headers=headers1,json=json_payload)
    data=response1.json()
    print(data)
    token=data["token"]
    print(type(token))
    return token

def test_put_requests():
    URL="https://restful-booker.herokuapp.com/booking/"
    booking_id="1449"
    pur_url=URL+booking_id
    cookie_value="token="+create_token()
    # print(cookie_value)
    headers={"Content-Type":"application/json",
             "Cookie":cookie_value}
    print(headers)
    json={
    "firstname" : "new123",
    "lastname" : "carsss123",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
    response2=requests.put(url=pur_url,headers=headers,json=json)
    assert response2.status_code==200
    data=response2.json()
    print(data)
    assert data["firstname"]=="new123","Incorrect Firstname"
    assert data["lastname"]=="carsss123","Incorrect Lastname"