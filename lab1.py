import requests

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
if not url.startswith('https://'): url = 'https://' + url
print(url)
