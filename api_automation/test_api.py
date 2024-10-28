import pytest
import requests
def test_get_request():
    id="512"
    url="https://restful-booker.herokuapp.com/booking/"
    full_url1=url+id
    response_body1=requests.get(full_url1)
    assert response_body1.status_code==200
    data1=response_body1.json()
    assert 'firstname' in data1,"Firstname is Not Present"
    assert 'lastname' in data1,"Lastname is Not Present"
    assert 'totalprice' in data1,"Totalprice is Not Present"
    assert 'depositpaid' in data1,"Depositpaid is Not Present"
    # assert 'checkin' in data1,"Checkin is Not Present"
    # assert 'checkout' in data1,"Checkout is Not Present"

    assert data1["firstname"]=="new","Incorrect Firstname"
    assert data1["lastname"]=="carsss","Incorrect Lastname"
    assert data1["totalprice"]==111,"Incorrect Totalprice"
    assert data1["depositpaid"]==True,"Incorrect Depositpaid"
    assert data1["bookingdates"]["checkin"]=="2018-01-01","Incorrect Checkin"
    assert data1["bookingdates"]["checkout"]=="2019-01-01","Incorrect Checkout"