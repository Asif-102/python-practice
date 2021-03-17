import requests

site = "http://www.linkforwardtrading.com/"

resp1 = requests.get('https://pastebin.com/raw/ng1BCyBf')

word_lists = resp1.content.split('\n')

for word in word_lists:
    admin=requests.get(site+word)
    out=admin.status_code
    if out==200:
        print(site+word)
