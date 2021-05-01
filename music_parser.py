import vk_api
from vk_api import audio
import requests
from time import time
from flask import jsonify

login = ''  # Номер телефона
password = ''  # Реально ВК замучали с регистрацией - надо вторую СИМ брать
#my_id = ''  # Ваш id vk

vk_session = vk_api.VkApi(login=login, password=password)
vk_session.auth()
vk = vk_session.get_api()  # Теперь можно обращаться к методам API как к обычным классам
vk_audio = audio.VkAudio(vk_session)  # Получаем доступ к audio


## Поиск музыки, принимает запрос и сдвиг       (логика сдвигов должны обсчитываться на клиенте)
def search(query, offset):
  result = []
  time_start = time()
  for data in vk_audio.search(query, count=5, offset=offset):
    try:
      result.append(data)
    except search_error:
        print(search_error + data["artist"] + '_' + data["title"]) # временно, надо бы логировать.

  time_finish = time()
  print("Time seconds:", time_finish - time_start)  # временно, надо бы логировать.
  return jsonify(result)

## Популярные, принимает сдвиг
def popular(offset):
  result = []
  time_start = time()
  for data in vk_audio.get_popular_iter(offset=offset):
    try:
      result.append(data)
    except popular_error:
        print(popular_error + data["artist"] + '_' + data["title"]) # временно, надо бы логировать.

  time_finish = time()
  print("Time seconds:", time_finish - time_start)  # временно, надо бы логировать.
  return jsonify(result)

## Новинки, принимает сдвиг - chomu to ne robit - nada kopat'sya v labe
def newsest(offset):
  result = []
  time_start = time()
  for data in vk_audio.get_news_iter(offset=offset):
    try:
      result.append(data)
    except newsest_error:
        print(search_error + data["artist"] + '_' + data["title"]) # временно, надо бы логировать.

  print(result)
  time_finish = time()
  print("Time seconds:", time_finish - time_start)  # временно, надо бы логировать.
  return jsonify(result)

## Музыка юзера - тут можно сделать готову подборку мб - хз зачем эта функция, поэтому убираем ее вниз
def user_(user_id):
  result = []
  time_start = time()
  for data in vk_audio.get(owner_id=user_id):
    try:
        result.append(data)

            #with open(data["artist"] + '_' + data["title"] + '.mp3', 'wb') as output_file:
            #output_file.write(response.content)    # 2 метода которые занимаются скачиванием - не нужны, нам нужно только формировать json и отдавать его фласку
    except user_error:
        print(user_error + data["artist"] + '_' + data["title"]) # временно, надо бы логировать.

  time_finish = time()
  print("Time seconds:", time_finish - time_start)  # временно, надо бы логировать.
  return jsonify(result)





