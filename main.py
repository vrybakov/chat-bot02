# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 21:06:28 2018

@author: 123
"""

import telebot
import cherrypy
import processing_all_message as p_a_m
import test_class
import additional_methods as add_m
import config
import StepNumber

from flask import Flask, request
import logging
import os

#
WEBHOOK_HOST = '151.101.86.49'
WEBHOOK_PORT = 443 # 443, 80, 88 или 8443 (порт должен быть открыт!)
WEBHOOK_LISTEN = '0.0.0.0'  # На некоторых серверах придется указывать такой же IP, что и выше
WEBHOOK_SSL_CERT = 'webhook_cert.pem'  # Путь к сертификату
WEBHOOK_SSL_PRIV = 'webhook_pkey.pem'  # Путь к приватному ключу

WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (config.token)





bot = telebot.TeleBot(config.token)


# Наш вебхук-сервер
class WebhookServer(object):
    @cherrypy.expose
    def index(self):
        if 'content-length' in cherrypy.request.headers and \
                        'content-type' in cherrypy.request.headers and \
                        cherrypy.request.headers['content-type'] == 'application/json':
            length = int(cherrypy.request.headers['content-length'])
            json_string = cherrypy.request.body.read(length).decode("utf-8")
            update = telebot.types.Update.de_json(json_string)
            # Эта функция обеспечивает проверку входящего сообщения
            bot.process_new_updates([update])
            return ''
        else:
            raise cherrypy.HTTPError(403)





#@bot.message_handler(commands = ['start'])
#def start_bot(message):
#    bot.send_message(message.chat.id, "Привет")
#


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message.chat.id, message.text)








# Проверим, есть ли переменная окружения Хероку (как ее добавить смотрите ниже)
#if "HEROKU" in list(os.environ.keys()):
#    logger = telebot.logger
#    telebot.logger.setLevel(logging.INFO)
#
#    server = Flask(__name__)
#    @server.route("/bot", methods=['POST'])
#    def getMessage():
#        bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
#        return "!", 200
#    @server.route("/")
#    def webhook():
#        bot.remove_webhook()
#        bot.set_webhook(url="127.0.0.1") # этот url нужно заменить на url вашего Хероку приложения
#        return "?", 200
#    server.run(host="0.0.0.0", port=os.environ.get('PORT', 80))
#else:
#    # если переменной окружения HEROKU нету, значит это запуск с машины разработчика.  
#    # Удаляем вебхук на всякий случай, и запускаем с обычным поллингом.
#    bot.remove_webhook()
#    bot.polling(none_stop=True)







#@bot.message_handler(commands = ['start'])
#def start_bot(message):
#    add_m.set_two_buttons("Привет!\nХочешь начать обучение гитаре?", "Да", "Нет", bot, message)
#    
#    StepNumber.newStep.add(config.Step_bot.STEP1.value)          
#    
#
#@bot.message_handler(content_types = ['text'])
#def test(message):
#    
#    obj = test_class.TestProcessingStage(message, StepNumber.newStep.get(), bot, "", False)
##    obj.stepS(p_a_m.a, "sad")
#    obj.answer_person("Да", config.Step_bot.STEP1.value).set_work_step(p_a_m.step1v1)
#    obj.answer_person("Нет", config.Step_bot.STEP1.value).set_work_step(p_a_m.step1v2)
##    obj.step1()
#    
#    obj.answer_person("Приступим к обучению с нуля", config.Step_bot.STEP2.value).set_work_step(p_a_m.step2v1)
#    obj.answer_person("Можно проверить мой уровень (не работает)", config.Step_bot.STEP2.value).set_work_step(p_a_m.step2v2)
##    obj.step2()
#    obj.answer_person("Да", config.Step_bot.STEP2_1.value).set_work_step(p_a_m.step2_1v1)
#    obj.answer_person("Нет", config.Step_bot.STEP2_1.value).set_work_step(p_a_m.step2_1v2)
#    obj.answer_person("Всё, готово", config.Step_bot.STEP2_1.value).set_work_step(p_a_m.step2_1v2)
#    
##    obj.step2_1()
#    obj.answer_person("Интересно узнать", config.Step_bot.STEP2_2.value).set_work_step(p_a_m.step2_2v1)
#    obj.answer_person("Не, я уже знаю как ее настроить", config.Step_bot.STEP2_2.value).set_work_step(p_a_m.step2_2v2)
#    obj.answer_person("Можем пойти дальше", config.Step_bot.STEP2_2.value).set_work_step(p_a_m.step2_2v2)
#
##    obj.step2_2()
#    obj.answer_person("Хорошо", config.Step_bot.STEP3.value).set_work_step(p_a_m.step3v1)
#    
#    
#    
#    
#    
#    
#    
#    
#    
#    
#    obj.unsuitable()
#
#    obj.step3()
#    S
    
    
    
# Снимаем вебхук перед повторной установкой (избавляет от некоторых проблем)
bot.remove_webhook()

 # Ставим заново вебхук
bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
                certificate=open(WEBHOOK_SSL_CERT, 'r'))
                
                
                
                
# Указываем настройки сервера CherryPy
cherrypy.config.update({
    'server.socket_host': WEBHOOK_LISTEN,
    'server.socket_port': WEBHOOK_PORT,
    'server.ssl_module': 'builtin',
    'server.ssl_certificate': WEBHOOK_SSL_CERT,
    'server.ssl_private_key': WEBHOOK_SSL_PRIV
})

 # Собственно, запуск!
cherrypy.quickstart(WebhookServer(), WEBHOOK_URL_PATH, {'/': {}})
#    
#if __name__ == '__main__':
#    bot.polling(none_stop = True) 