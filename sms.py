import requests
import time

Enter = input("enter number")
url = "https://mc.yandex.ru/watch/94212660/1?page-url=https%3A%2F%2Fapp.snapp.taxi%2Flogin&c"
while True:
    time.sleep(3)
    number = {"cellphone":"+98"+Enter}
    sms = requests.post(url,data=number)
    print(sms.status_code)
