import random
import requests
import names

count = 0

def main(num):
    for i in range(num):
        arbys(domain)

def arbys(email):
    global count
    s = requests.Session()
    url = "https://arbys.fbmta.com/members/subscribe.aspx"
    name = names.get_full_name().replace(" ", "")
    num = random.randint(1,9999)
    email = name + str(num) + "@" + domain

    headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "arbys.fbmta.com",
    "Origin": "https://arbys.com",
    "Referer": "https://arbys.com/get-deals"
    }

    payload = {

        "ListID": "27917287443",
        "SiteGUID": "220b8a14-335c-42e0-8b07-1dfe8ec259cd",
        "_Theme": "27917287575",
        "InputSource": "W-Mobile",
        "Birthdate": "",
        "FirstName": names.get_first_name(),
        "LastName": names.get_first_name(),
        "EmailAddress": email,
        "Zip": "98499",
        "StoreCode": "00413",
        "DOBM": "2",
        "DOBD": "6",
        "OverThirteen": True,
        "MobilePhone": ""
    }

    r = s.post(url,data=payload,headers=headers)
    if "Thank You!" in r.content:
        count+=1
        print("Successfully obtained deal for {} - Count = {}".format(email,count))
        account = open("emails.txt", "a")
        account.write(email + "\n")
    else:
        arbys()
        print("Retrying...")


if __name__ == '__main__':
    print("ARBYS SCRIPT CREATED BY KENNYD")
    print("+++++++++++++++++++++++")
    domain = raw_input('Enter your domain w/ no @ (ex. github.com): ')
    num = int(raw_input('Amount: '))

    main(num)
