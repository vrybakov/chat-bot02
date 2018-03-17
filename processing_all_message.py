# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 21:06:54 2018

@author: 123
"""

import additional_methods as add_m
import dbworker
import config
import StepNumber as s_n


def step1v1(message, bot):
    add_m.send_message("Отлично!\nДля того, чтобы начать обучение, нам необходимо узнать твой навык игры на гитаре.", bot, message)
    add_m.set_two_buttons("Можем устроить проверку или сразу начать обучение с нуля\nЧто выберешь?",
                          "Приступим к обучению с нуля",
                          "Можно проверить мой уровень (не работает)", bot, message)
    s_n.newStep.add(config.Step_bot.STEP2.value)      
#    dbworker.set_state(message.chat.id, config.Step_bot.STEP2.value)
        
def step1v2(message, bot):
    bot.send_message(message.chat.id, "Твое дело.")
    
###   
    

def step2v1(message, bot):
    add_m.set_two_buttons("Давай я тебе покажу устройство гитары, если тебе это интересно.", "Да", "Нет", bot, message)
    s_n.newStep.add(config.Step_bot.STEP2_1.value)    
#    dbworker.set_state(message.chat.id, config.Step_bot.STEP2_1.value)
        
def step2v2(message, bot):
    bot.send_message(message.chat.id, "Пройдем тесты. (не рабоает)")
###
    
def step2_1v1(message, bot):
    bot.send_message(message.chat.id, "На этом изображение подробно показано строение гитары")
    photo = open('image/guitar structure.jpg', 'rb') #открывает изображение
    bot.send_photo(message.chat.id, photo)    #отправляет сообщение с изображением
    add_m.set_one_button("Скажи, когда разберешься.",
                         "Всё, готово", bot, message)
    s_n.newStep.add(config.Step_bot.STEP2_1.value)    
#    dbworker.set_state(message.chat.id, config.Step_bot.STEP2_1.value)
        
def step2_1v2(message, bot):
    add_m.set_two_buttons("Хочешь узнать, как можно настроить гитару?",
                          "Интересно узнать",
                          "Не, я уже знаю как ее настроить", bot, message)
    s_n.newStep.add(config.Step_bot.STEP2_2.value)                          
#    dbworker.set_state(message.chat.id, config.Step_bot.STEP2_2.value)
    
###
def step2_2v1(message, bot):
        add_m.send_link("Посмореть видео", "https://www.youtube.com/watch?v=iAZkTAc_2E0",
                        "Нажми сюда, чтобы посмотреть, какие есть методы.", bot, message)
        add_m.set_one_button("Если разобрались, то скажи, что можно идти дальше.",
                             "Можем пойти дальше", bot, message)
        s_n.newStep.add(config.Step_bot.STEP2_2.value)    
#        dbworker.set_state(message.chat.id, config.Step_bot.STEP2_2.value)
        
def step2_2v2(message, bot):
        add_m.set_one_button("Тогда далее поэтапно будем учиться играть.\nНаш курс буде разбит на 5 этапов от простого к сложному.",
                             "Хорошо", bot, message)
        s_n.newStep.add(config.Step_bot.STEP3.value)    
#        dbworker.set_state(message.chat.id, config.Step_bot.STEP3.value)
        
        
###
def step3v1(message, bot):
        add_m.set_two_buttons("Давай перейдем к первому этапу.",
                              "Давай",
                              "Нет, я все же хочу вернуться назад", bot, message)
        s_n.newStep.add(config.Step_bot.STEP4_STAGE1.value)    
#        dbworker.set_state(message.chat.id, config.Step_bot.STEP4_STAGE1.value)
        
def step3v2(message, bot):
        add_m.send_message("Я рад, что ты уже на втором этапе, дальше буде только интереснее.", bot, message)
        add_m.set_one_button("Нажми далее, чтобы мы смогли приступить.",
                              "Далее",
                              bot, message)
        s_n.newStep.add(config.Step_bot.STEP3.value)    
#        dbworker.set_state(message.chat.id, config.Step_bot.STEP3.value)
### 
def unsuitable(message, bot):
    bot.send_message(message.chat.id, "Что-то не то. Попробуй повторить.")