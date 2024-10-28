import requests
import pytest
@pytest.mark.positive
def test_create_booking_positive():
    print("Create Booking Testcase")
    URL="https://restful-booker.herokuapp.com/booking"
    headers={"Content-Type":"application/json"}
    json={
    "firstname" : "new",
    "lastname" : "carsss",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
    response=requests.post(url=URL,headers=headers,json=json)
    assert response.status_code==200
    data=response.json()
    booking_id=data["bookingid"]
    print(booking_id)
    assert data["bookingid"] is not None
    assert data["booking"]["firstname"]=="new","Incorrect FirstName"
    assert data["booking"]["lastname"]=="carsss","Incorrect LastName"

@pytest.mark.negative
def test_create_booking_negative():
    print("Create Booking Testcase")
    URL="https://restful-booker.herokuapp.com/booking"
    headers={"Content-Type":"application/json"}
    json={}
    response=requests.post(url=URL,headers=headers,json=json)
    assert response.status_code==500
