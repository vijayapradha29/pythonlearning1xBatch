import requests
import pytest

def create_token():
    url="https://restful-booker.herokuapp.com/auth"
    json={
    "username" : "admin",
    "password" : "password123"
}
    headers1={"Content-Type":"application/json"}
    res=requests.post(url=url,headers=headers1,json=json)
    data=res.json()
    token=data["token"]
    print(token)
    return token
def create_booking():
    url="https://restful-booker.herokuapp.com/booking"
    headers_new={"Content-Type":"application/json"}
    json={
    "firstname" : "123",
    "lastname" : "456",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
    res2=requests.post(url=url,headers=headers_new,json=json)
    assert res2.status_code==200
    data_new=res2.json()
    booking_id=data_new["bookingid"]
    print(booking_id)
    assert data_new["bookingid"] is not None
    assert data_new["booking"]["firstname"]=="123","Incorrect Firstname"
    assert data_new["booking"]["lastname"]=="456","Incorrect Lastname"
    return booking_id
def test_get_requests():
    url="https://restful-booker.herokuapp.com/booking/"
    id=create_booking()
    ful_url=url+str(id)
    response=requests.get(url=ful_url)
    data1=response.json()
    assert response.status_code==200
    assert 'firstname' in data1,"Incorrect Firstname"
    assert 'lastname' in data1,"Incorrect Lastname"
    assert data1["firstname"]=="123","Incorrect Firstname Data"
    assert data1["lastname"]=="456","Incorrect Lastname Data"
    assert data1["bookingdates"]["checkin"]=="2018-01-01","Incorrect Checkin Dates"
def test_put_requests():
    url_new="https://restful-booker.herokuapp.com/booking/"
    id_new=create_booking()
    full_url_new=url_new+str(id_new)
    json={
    "firstname" : "123",
    "lastname" : "456",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
    cookie_value="token="+create_token()
    print(cookie_value)
    headers_new1 = {"Content-Type": "application/json","Cookie":cookie_value}
    res1=requests.put(url=full_url_new,headers=headers_new1,json=json)
    assert res1.status_code==200
    data=res1.json()
    assert data["firstname"]=="123","Incorrect Firstname"
    assert data["lastname"]=="456","Incorrect Lastname"
def test_delete():
    url="https://restful-booker.herokuapp.com/booking/"
    id=create_booking()
    full_url_new=url+str(create_booking())
    cookie_value_new="token="+create_token()
    headers_new={"Content-Type":"application/json","Cookie":cookie_value_new}
    response_new=requests.delete(url=full_url_new,headers=headers_new)
    assert response_new.status_code==201
