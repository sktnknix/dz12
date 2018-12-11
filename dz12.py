# -*- coding: utf-8 -*-

import requests

class User():
    def __init__(self, token):
        self.id = input('Enter id: ')
        self.token = token

    def __and__(self, fr_list1, fr_list2):
        self.fr_list1 = fr_list1
        self.fr_list2 = fr_list2
        return fr_list1 & fr_list2

    def __str__(self):
        link = 'https://vk.com/id' + str(self.id)
        return link

    def get_friends(self, count):
        params = {
            'user_id': self.id,
            'access_token': self.token,
            'v': '5.92',
            'count': count,
            'fields': 'nickname'
        }
        response = requests.get('https://api.vk.com/method/friends.get', params)
        return response.json()


token = '0c72675649b9a8d1051bdd5e6da165f32e0836b4dbbde9887687533d9c9761e094a1f3ddcb8eeb3459c90'

oleg = User(token)
ivan = User(token)
oleg_friends = oleg.get_friends(1000)
ivan_friends = ivan.get_friends(1000)
oleg_set = {(item['first_name'] + ' ' + item['last_name'], item['id']) for item in oleg_friends['response']['items']}
ivan_set = {(item['first_name'] + ' ' + item['last_name'], item['id']) for item in ivan_friends['response']['items']}
vladimir = User(token)
res = vladimir.__and__(oleg_set, ivan_set)
print(res)
print('Enter id for print his vk link: ' + str(User(token)))


