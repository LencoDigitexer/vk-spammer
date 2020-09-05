#!/usr/bin/python
# Author: https://vk.com/id181265169

import vk, urllib.request, urllib.error, urllib.parse, json, random, time

username = input("Login:")
password = input("Password:")

url = "https://oauth.vk.com/token?grant_type=password&client_id=3697615&client_secret=AlVXZFMUqyrnABp8ncuU&username=%s&password=%s" % (username, password)

try:
    r = urllib.request.urlopen(url)
except urllib.error.HTTPError:
    print("Возможно, неправильный пароль")
    quit(1)

r = r.read()
token = json.loads(r)["access_token"] 
'''
session = vk.Session(access_token = token)
vk = vk.API(session)
'''

try:
    foo = open('dict.txt', 'r', encoding='utf-8').read().splitlines()
except IOError:
    open('dict.txt', 'w', encoding='utf-8')
    print("Словарь спама отсутствует. Был создан пустой dict.txt")




# print (foo)
print("Вы можете ввести id юзера или id беседы")
victim = input("Peer id: ")
victim = int(2000000000) + int(victim)
'''
r = vk.users.get(peer_id = victim, fields = "id", v = 5.73)
r = r[0]["id"]
'''



for i in range(0, len(foo)):
	try:
		time.sleep(random.randint(1,3) + random.randint(1,4))
		#r = vk.messages.send(peer_id = victim, message = str(foo[i]), v = 5.73)
		r = urllib.request.urlopen("http://api.vk.com/method/messages.send?access_token={0}&message={1}&peer_id={2}&random_id={3}&v=5.101".format(token, str(foo[i]), victim, random.randint(1,2700) + random.randint(1,2700)))
		print()
		print("wait...")
		time.sleep(random.randint(1,2) + random.randint(1,2))
		print("done  ", str(foo[i]))
	except:
		pass