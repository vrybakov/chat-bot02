# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 11:25:36 2018

@author: 123
"""
f = "file_id.ini"




class StepNumber:
    def add(self, name_button):
        file_id = open(f, "w")
        file_id.write(name_button)
        file_id.close()
        
    def get(self):
        file_id = open(f)
        _get_step = file_id.read()
        file_id.close()
        return _get_step
newStep = StepNumber()