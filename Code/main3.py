import json
from urllib.request import urlopen

import dns.resolver
import requests

if __name__ == '__main__':
    url = 'python.org'
    ip = dns.resolver.resolve(url, 'A')
    for i in ip:
        print('IP', i.to_text())
    name = dns.reversename.from_address('138.197.63.241')
    print(name)
    print(dns.reversename.to_address(name))
    # url = 'http://ipinfo.io/json'
    # url = 'https://geolocation-db.com/jsonp/'
    # r = urlopen(url)
    # r = requests.get(url)
    # data = r.content.decode()
    # data = data.split("(")[1].strip(")")
    # data = json.loads(data)
    # print(data)
    # ip = data['ip']
    # org = data['org']
    # city = data['city']
    # country = data['country']
    # region = data['region']
    # print(ip, org, city, country, region)