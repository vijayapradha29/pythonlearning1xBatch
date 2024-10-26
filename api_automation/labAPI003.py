import requests


def main():
    response_body = requests.get("https://restful-booker.herokuapp.com/booking/461")
    assert response_body.status_code==200



if __name__ == '__main__':
    main()
