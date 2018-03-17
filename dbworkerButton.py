# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 00:06:19 2018

@author: 123
"""

from vedis import Vedis

# Пытаемся узнать из базы «состояние» пользователя
def get_current_button(user_id, db_file):
    with Vedis(db_file) as db:
        try:
            return db[user_id.chat.id]
        except KeyError:  # Если такого ключа почему-то не оказалось
            return 0  # значение по умолчанию - начало диалога

# Сохраняем текущее «состояние» пользователя в нашу базу
def set_button(user_id, db_file, value):
    with Vedis(db_file) as db:
        try:
            db[user_id.chat.id] = value
            return True
        except:
            # тут желательно как-то обработать ситуацию
            return False