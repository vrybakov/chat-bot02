# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 16:37:07 2018

@author: 123
"""
import telebot
import config
bot = telebot.TeleBot(config.token)


@bot.message_handler(commands = ['start'])
def start_bot(message):
    bot.send_message(message.chat.id, "Привет")
    
    
if __name__ == '__main__':
    bot.polling(none_stop = True) 