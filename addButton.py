# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 11:25:36 2018

@author: 123
"""

class Button:
    _button = []
    def add(self, name_button):
        self._button.append(name_button)
        return self
newButton = Button()