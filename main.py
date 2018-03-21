# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 21:06:28 2018

@author: 123
"""

import telebot
import processing_all_message as p_a_m
import test_class
import additional_methods as add_m
import config
import StepNumber

from flask import Flask, request
import logging
import os
#
##






bot = telebot.TeleBot(config.token)






#
#@bot.message_handler(commands = ['start'])
#def start_bot(message):
#    bot.send_message(message.chat.id, "Привет")



#@bot.message_handler(func=lambda message: True, content_types=['text'])
#def echo_message(message):
#    bot.reply_to(message.chat.id, message.text)




@bot.message_handler(commands = ['start'])
def start_bot(message):
    add_m.set_two_buttons("Привет!\nХочешь начать обучение гитаре?", "Да", "Нет", bot, message)
    
    StepNumber.newStep.add(config.Step_bot.STEP1.value)          
    

@bot.message_handler(content_types = ['text'])
def test(message):
    
    obj = test_class.TestProcessingStage(message, StepNumber.newStep.get(), bot, "", False)
#    obj.stepS(p_a_m.a, "sad")
    obj.answer_person("Да", config.Step_bot.STEP1.value).set_work_step(p_a_m.step1v1)
    obj.answer_person("Нет", config.Step_bot.STEP1.value).set_work_step(p_a_m.step1v2)
#    obj.step1()
    
    obj.answer_person("Приступим к обучению с нуля", config.Step_bot.STEP2.value).set_work_step(p_a_m.step2v1)
    obj.answer_person("Можно проверить мой уровень (не работает)", config.Step_bot.STEP2.value).set_work_step(p_a_m.step2v2)
#    obj.step2()
    obj.answer_person("Да", config.Step_bot.STEP2_1.value).set_work_step(p_a_m.step2_1v1)
    obj.answer_person("Нет", config.Step_bot.STEP2_1.value).set_work_step(p_a_m.step2_1v2)
    obj.answer_person("Всё, готово", config.Step_bot.STEP2_1.value).set_work_step(p_a_m.step2_1v2)
    
#    obj.step2_1()
    obj.answer_person("Интересно узнать", config.Step_bot.STEP2_2.value).set_work_step(p_a_m.step2_2v1)
    obj.answer_person("Не, я уже знаю как ее настроить", config.Step_bot.STEP2_2.value).set_work_step(p_a_m.step2_2v2)
    obj.answer_person("Можем пойти дальше", config.Step_bot.STEP2_2.value).set_work_step(p_a_m.step2_2v2)

#    obj.step2_2()
    obj.answer_person("Хорошо", config.Step_bot.STEP3.value).set_work_step(p_a_m.step3v1)
    
    
    
    
    
    
    
    
    
    
    obj.unsuitable()

    

# Проверим, есть ли переменная окружения Хероку (как ее добавить смотрите ниже)
if "HEROKU" in list(os.environ.keys()):
    logger = telebot.logger
    telebot.logger.setLevel(logging.INFO)

    server = Flask(__name__)
    @server.route("/bot", methods=['POST'])
    def getMessage():
        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
        return "!", 200
    @server.route("/")
    def webhook():
        bot.remove_webhook()
        bot.set_webhook(url="https://dashboard.heroku.com/apps/calm-ravine-51322") # этот url нужно заменить на url вашего Хероку приложения
        return "?", 200
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 80))
else:
    # если переменной окружения HEROKU нету, значит это запуск с машины разработчика.  
    # Удаляем вебхук на всякий случай, и запускаем с обычным поллингом.
    bot.remove_webhook()
    bot.polling(none_stop=True)



#if __name__ == '__main__':
#    bot.polling(none_stop = True) 