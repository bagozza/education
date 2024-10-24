import requests

"""Requests позволяют очень легко отправлять HTTP/1.1-запросы. Пользоваться request чрезвычайно легко.
Вам не нужно вручную добавлять строки запроса в URL-адреса или кодировать данные POST"""

response = requests.get('https://api.github.com')
print(response.json())
print("\n код requests \n")

"""Код без использования requests"""


import urllib2

gh_url = 'https://api.github.com'

req = urllib2.Request(gh_url)

password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_manager.add_password(None, gh_url, 'user', 'pass')

auth_manager = urllib2.HTTPBasicAuthHandler(password_manager)
opener = urllib2.build_opener(auth_manager)

urllib2.install_opener(opener)

handler = urllib2.urlopen(req)

print handler.getcode()
print handler.headers.getheader('content-type')



"""Код с использованием requests"""

import requests

r = requests.get('https://api.github.com', auth=('user', 'pass'))

print r.status_code
print r.headers['content-type']
