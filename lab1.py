import requests
from time import datetime

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break

#url = 'http://python.org/'  

#with requests.get(url) as response: 
#    html = response.text
#    more(html)

url = input('Enter URL: ')
if not url.startswith('https://'):
    url = 'https://' + url
print(url)

with requests.get(url) as response: 
#    for key in response.headers:
#        print(f"{key}: {response.headers[key]}")
#   1o
    print(f"Server: {response.headers.get('Server')}")
#   2o
    print(f"Has cookies: {'Set-Cookie' in response.headers}")
    for cookie in response.cookies:
        print(f"Name: {cookie.name}, Expires: {datetime.fromtimestamp(cookie.expires)}")