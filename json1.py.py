import json
import requests

posts = json.loads(requests.get('https://jsonplaceholder.typicode.com/posts').content)
comments = json.loads(requests.get('https://jsonplaceholder.typicode.com/comments').content)
user_posts = list(map(lambda p: {**p, 'comments': list(filter(lambda c: c.get('id') == p.get('id'), comments))}, posts))


def get_user_data(uid):
  return list(filter(lambda p: p.get('userId') == uid, user_posts))




a=int(input("please enter id want to show whose posts and comments\n"))

print(get_user_data(uid=a))



input("pres any key to exit")


'''import urllib.request
import json

url = 'https://jsonplaceholder.typicode.com/posts'

def response(url):
    with urllib.request.urlopen(url) as response:
        return response.read()

res = json.loads(response(url)) 
print(res)
names = list(map(lambda n : n.get('userId'),res.get(' ')))
print(names)'''
