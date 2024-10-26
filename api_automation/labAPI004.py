import requests
def main():
    id=3220
    url="https://restful-booker.herokuapp.com/booking/"
    full_url=url+str(id)
    response_body=requests.get(full_url)
    assert response_body.status_code==200
    data = response_body.json()
    assert 'firstname' in data, "Firstname is Present"
    assert 'lastname' in data, "LastName is Present"
    assert data["firstname"]=="busss","busss is Present"
    assert data["lastname"]=="carsss","carsss is Present"
    assert data["bookingdates"]["checkin"]=="2018-01-01","checkin is Present"


if __name__ == '__main__':
    main()