import requests


def main():
    response_body = requests.get("https://restful-booker.herokuapp.com/booking/3220")
    print(response_body.text)
    print(response_body.status_code)
    # print(response_body.json())
    #verify or write test cases to verify:
    if response_body.status_code == 200:
        print("TC#1-Verify that GET Requests is Successful")
    else:
        print("TC#1-Verify that GET Requests is Not Successful")


if __name__ == "__main__":
    main()
