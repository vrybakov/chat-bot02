# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 12:53:16 2018

@author: 123
"""


from telebot import types

import dbworkerButton as db



#Отправляет сообщение чат-бот
def send_message(answer, bot, message):
    bot.send_message(message.chat.id, answer) 
    
#Создает кнопки для отправки ответа пользователем
#одна кнопка

    
def set_one_button(answer, text_button, bot, message):
        button = types.ReplyKeyboardMarkup()
        button.row(text_button)
        bot.send_message(message.chat.id, answer, reply_markup = button)

#две кнопки        
def set_two_buttons(answer, text_button_1, text_button_2, bot, message):
        button = types.ReplyKeyboardMarkup()
        button.row(text_button_1)
        button.row(text_button_2)
        bot.send_message(message.chat.id, answer, reply_markup = button)

#        b.button = "sad"
        
#три кнопки        
def set_three_buttons(answer, text_button_1, text_button_2, text_button_3, bot, message):
        button = types.ReplyKeyboardMarkup()
        button.row(text_button_1)
        button.row(text_button_2)
        button.row(text_button_3)        
        bot.send_message(message.chat.id, answer, reply_markup = button)
        
        
#четыре кнопки        
def set_four_buttons(answer, text_button_1, text_button_2, text_button_3, text_button_4, bot, message):
        button = types.ReplyKeyboardMarkup()
        button.row(text_button_1)
        button.row(text_button_2)
        button.row(text_button_3)
        button.row(text_button_4)
        bot.send_message(message.chat.id, answer, reply_markup = button)
        
#кнопка в виде ссылке        
def send_link(name_link, link, text, bot, message):
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(name_link, link)
        keyboard.add(url_button)
        bot.send_message(message.chat.id, text, reply_markup = keyboard)