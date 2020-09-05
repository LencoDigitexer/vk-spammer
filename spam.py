#!/usr/bin/python
# Author: https://vk.com/id181265169

import vk, urllib.request, urllib.error, urllib.parse, json, random, time

username = input("Login:")
password = input("Password:")

url = "https://oauth.vk.com/token?grant_type=password&client_id=3697615&client_secret=AlVXZFMUqyrnABp8ncuU&username=%s&password=%s" % (username, password)

try:
    r = urllib.request.urlopen(url)
except urllib.error.HTTPError:
    print("�� ���������� �������������� (�������� ����������� ������� ����� ��� ������)")
    quit(1)

r = r.read()
token = json.loads(r)["access_token"] 
session = vk.Session(access_token = token)
vk = vk.API(session)


try:
    foo = open('dict.txt', 'r', encoding='utf-8').read().splitlines()
except IOError:
    open('dict.txt', 'w', encoding='utf-8')
    print("Словарь спама отсутствует. Был создан пустой dict.txt")




# print (foo)

victim = input("User id: ")

r = vk.users.get(user_id = victim, fields = "id", v = 5.73)
r = r[0]["id"]

victim = r

for i in range(0, len(foo)):
	try:
		time.sleep(random.randint(1,3) + random.randint(1,4))
		r = vk.messages.send(peer_id = victim, message = str(foo[i]), v = 5.73)
		print()
		print("wait...")
		time.sleep(random.randint(1,2) + random.randint(1,2))
		print("done  ", str(foo[i]))
	except:
		pass