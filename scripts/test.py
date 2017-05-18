import requests
id = -456246072
for i in range (1):
    r = requests.get('https://api.vk.com/method/groups.search' ,params={'q': ''})
    res = r.json()
    print(res)