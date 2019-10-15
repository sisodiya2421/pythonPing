import requests

class webpage():
    def __init__(self, link, time):
        self.link = link
        self.time = time

def get_request(webpage):
    url = webpage
    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"}
    response = requests.get(url, headers=headers)
    print(response)
