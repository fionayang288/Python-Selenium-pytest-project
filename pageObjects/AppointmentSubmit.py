# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 20:32:46 2020

@author: fiona
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass

class ConfirmBookingPage:
        
    def __init__(self,driver):
        self.driver=driver
    