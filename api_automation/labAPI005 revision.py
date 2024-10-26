import requests
def main():
    response_body=requests.get("https://restful-booker.herokuapp.com/booking/161")
    print(response_body.text)
    print(response_body.status_code)
    # print(response_body.json())
    if response_body.status_code==200:
        print("TC#1-Verify Status Code as 200 Successful")
    else:
        print("TC#1-Verify Status Code as 200 Not Successful")
if __name__ == '__main__':
    main()