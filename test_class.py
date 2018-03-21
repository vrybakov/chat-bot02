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
