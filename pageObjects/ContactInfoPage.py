# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 20:17:53 2020

@author: fiona
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass

class ContactInfoPage:
    
    def __init__(self,driver,emailaddress,phone):
        self.driver=driver
        self.emailaddress=emailaddress
        self.phone=phone
    
    def fillContactInfo(self):
        self.driver.find_element_by_xpath("//input[@name='EmailAddress']").send_keys(self.emailaddress)
        self.driver.find_element_by_xpath("//input[@name='PhoneNumber']").send_keys(self.phone)
        
        self.driver.find_element_by_xpath("//input[@name='SelectedContacts[0].IsSelected' and @type='checkbox']").click()
        self.driver.find_element_by_xpath("//input[@name='SelectedContacts[2].IsSelected' and @type='checkbox']").click()
        
        return self.driver.find_element_by_name("Next")

