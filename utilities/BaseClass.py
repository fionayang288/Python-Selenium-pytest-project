# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 15:15:16 2020

@author: fiona
"""

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import inspect
import logging

@pytest.mark.usefixtures("setup","getData")
class BaseClass:
#    self.first_name=getData["first_name"]
#    self.last_name=getData["last_name"]
#    self.emailaddress=getData["emailaddress"]
#    self.service=getData["service"]
#    self.phone=getData["phone"]
#    self.office=getData["office"]
#    self.choose_date=getData["choose_date"]
#    self.timeslot=getData["timeslot"]
        
    def verifyLinkPresense(self,text):
        element=WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.LINK_TEXT,text)))
        
    #select an option from dropdown
    def selectOptionByText(self,locator,text):
        sel=Select(locator)
        sel.select_by_visible_text(text)
    
    def getLogger(self):
        loggerName=inspect.stack()[1][3]
        logger=logging.getLogger(loggerName)
        fileHandler=logging.FileHandler('logfile.log')
        formatter=logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        
        logger.addHandler(fileHandler)
        
        logger.setLevel(logging.DEBUG)
        return logger



