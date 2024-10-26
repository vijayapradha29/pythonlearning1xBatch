import requests
def main():
    response_body=requests.get("https://restful-booker.herokuapp.com/booking/161")
    assert response_body.status_code==200,"Not Successful"
    data=response_body.json()
    assert 'firstname' in data,"FirstName is Not Present"
    assert 'lastname' in data,"LastName is Not Present"
    assert data["firstname"]=="busss","busss is Not Present"
    assert data["lastname"]=="carsss","carsss is Not Present"
    assert data["bookingdates"]["checkin"]=="2018-01-01","2018-01-01 is Not Present"
if __name__ == '__main__':
    main()