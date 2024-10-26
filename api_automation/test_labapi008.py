import pytest
import requests
def test_sample():
    assert 4==4
def test_sample1():
    assert 5==5
def test_getrequest():
    response_body=requests.get("https://restful-booker.herokuapp.com/booking/3803")
    assert response_body.status_code==200
    data=response_body.json()
    assert 'firstname' in data,"Firstname is Not Present"
    assert 'lastname' in data,"Lastname is Not Present"

    assert data["firstname"]=="new","Incorrect Firstname"
    assert data["lastname"]=="carsss","Incorrect Lastname"
    assert data["bookingdates"]["checkin"]=="2018-01-01","Incorrect Date"
