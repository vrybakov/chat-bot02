# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 21:49:17 2018

@author: 123
"""


class TestProcessingStage:
    def __init__ (self, message, step, bot, current_step, un):
        self.message = message
        self.step = step
        self.bot = bot
        self.current_step = current_step
        self.un = un

    def answer_person(self, ans, current_step):
        self.ans = ans
        self.current_step = current_step
        return self
        
    def set_work_step(self, func):
        if self.step == self.current_step:
            if self.message.text == self.ans:
                self.un = True
                func(self.message, self.bot)
        return self
        
        
    def unsuitable(self):
        if self.un == False:
            self.bot.send_message(self.message.chat.id, "Что-то не то. Попробуй повторить.")

    
#    def step1(self):
#        if self.step == config.Step_bot.STEP1.value:
#            db.get_current_button(self.message, add_m.button1)
#            if self.message.text == "Да":
#                p_a_m.step1v1(self.message, self.bot)
#            elif self.message.text == "Нет":
#                p_a_m.step1v2(self.message, self.bot)
#            else:
#                p_a_m.unsuitable(self.message, self.bot)
#                
#                
#                
#                
#    def step2(self):
#        if self.step == config.Step_bot.STEP2.value:
#            if self.message.text == "Приступим к обучению с нуля":
#                p_a_m.step2v1(self.message, self.bot)
#            elif self.message.text == "Можно проверить мой уровень (не работает)":
#                p_a_m.step2v2(self.message, self.bot)
#            else:
#                p_a_m.unsuitable(self.message, self.bot)
#                
#                
#    def step2_1(self):
#        if self.step == config.Step_bot.STEP2_1.value:
#            if self.message.text == "Да":
#                p_a_m.step2_1v1(self.message, self.bot)
#            elif self.message.text == "Нет" or self.message.text == "Всё, готово":
#                p_a_m.step2_1v2(self.message, self.bot)
#            else:
#                p_a_m.unsuitable(self.message, self.bot)
#
#    def step2_2(self):
#        if self.step == config.Step_bot.STEP2_2.value:
#            if self.message.text == "Интересно узнать":
#                p_a_m.step2_2v1(self.message, self.bot)
#            elif self.message.text == "Не, я уже знаю как ее настроить" or self.message.text == "Можем пойти дальше":
#                p_a_m.step2_2v2(self.message, self.bot)
#            else:
#                p_a_m.unsuitable(self.message, self.bot)
#                
#    def step3(self):
#        if self.step == config.Step_bot.STEP3.value:
#            if self.message.text == "Хорошо":
#                p_a_m.step3v1(self.message, self.bot)
#            elif self.message.text == "Не, я хочу перейти на второй этап":
#                p_a_m.step3v2(self.message, self.bot)
#            else:
#                p_a_m.unsuitable(self.message, self.bot)
        
#    def sendMessage(self, step):
#        if config.Step_bot.STEP1.value == dbworker.get_current_state(step):
#            p_a_m.step1()
#    def messageToSend(self):
        