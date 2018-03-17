# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 23:57:38 2018

@author: 123
"""

from enum import Enum

token = '481180883:AAFjGPMJVPKL0xaH2MksG4GlH5bprwwxdpI'
db_file = "database.vdb"
db_file_copy = "database_copy.vdb"

    
class Step_bot(Enum):
    
    START = "0"
    STEP1 = "1"
    STEP2 = "2"
    STEP2_1 = "2.1"
    STEP2_2 = "2.2"
    STEP2_3 = "2.3"
    STEP3 = "3"
    STEP4_STAGE1 = "4s1"
    STEP4_1_STAGE1 = "4.1s1"
    STEP4_2_STAGE1 = "4.2s1"
    STEP4_3_STAGE1 = "4.3s1"
    STEP4_4_STAGE1 = "4.4s1"    
    STEP4_5_STAGE1 = "4.5s1"
    STEP4_6_STAGE1 = "4.6s1"        
    
    
    STEP_BREAK = "s_b"
