# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 20:04:08 2020

@author: fiona
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass
from pageObjects.ContactInfoPage import ContactInfoPage

class NamePage:
    
    def __init__(self,driver,first_name,last_name,emailaddress,phone):
        self.driver=driver
        self.first_name=first_name
        self.last_name=last_name
        self.emailaddress=emailaddress
        self.phone=phone
        
    
    def fillName(self):
        self.driver.find_element_by_name("Customers[0].BookingFieldValues[0].Value").send_keys(self.first_name)
        self.driver.find_element_by_name("Customers[0].BookingFieldValues[1].Value").send_keys(self.last_name)
        self.driver.find_element_by_name("Next").click()
        
        return ContactInfoPage(self.driver,self.emailaddress,self.phone)
    