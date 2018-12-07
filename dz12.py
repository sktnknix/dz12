# -*- coding: utf-8 -*-

import requests

class User:
    def __init__(self, token):
        self.token = token

    def __add__(self, fr_list1, fr_list2):
        self.fr_list1 = fr_list1
        self.fr_list2 = fr_list2
        return fr_list1 & fr_list2

    def __str__(self):
        link = 'https://vk.com/id' + str(id)
        return link

    def get_friends(self, count, id):
        params = {
            'user_id': id,
            'access_token': self.token,
            'v': '5.92',
            'count': count,
            'fields': 'nickname'
        }
        response = requests.get('https://api.vk.com/method/friends.get', params)
        return response.json()


token = '18bd7fdb217b99223689d2e63f496a7907a8ed437c4771d5c948df4cf683fd4ba6403ce7297f220052afa'

oleg = User(token)
ivan = User(token)
oleg_friends = oleg.get_friends(1000, 5737666)
ivan_friends = ivan.get_friends(1000, 23426294)
oleg_set = {(item['first_name'] + ' ' + item['last_name'], item['id']) for item in oleg_friends['response']['items']}
ivan_set = {(item['first_name'] + ' ' + item['last_name'], item['id']) for item in ivan_friends['response']['items']}
vladimir = User(token)
res = vladimir.__add__(oleg_set, ivan_set)
print(res)
id = 520282900
print(User(token))


