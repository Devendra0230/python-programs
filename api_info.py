import requests


class Find_ip():
    def __init__(self):
        # ip address in text formate
        self.ip_add = requests.get('https://api.ipify.org').text

        print("Your IP Address is :", self.ip_add)

    def ip_details(self):
        # find information of IP add
        res = requests.get(f'http://ip-api.com/json/{self.ip_add}?fields=1049087').json()
        # http://ip-api.com/json/{self.ip_add}?

        for x, y in res.items():
            print(x, ':', y)


ip_add = Find_ip()
ip_add.ip_details()
