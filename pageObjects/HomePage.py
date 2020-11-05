# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 15:40:14 2020

@author: fiona
"""
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass

from pageObjects.AcceptInfoPage import AcceptInfoPage

class HomePage:
        
    def __init__(self,driver,service,choose_date,timeslot,office,\
                 first_name,last_name,emailaddress,phone):
        self.driver=driver
        self.service=service
        self.choose_date=choose_date
        self.timeslot=timeslot
        self.office=office
        self.first_name=first_name
        self.last_name=last_name
        self.emailaddress=emailaddress
        self.phone=phone
    
    def selectService(self):
        locator=self.driver.find_element_by_id("ServiceGroupId")
        BaseClass.selectOptionByText(self,locator,self.service)
        self.driver.find_element_by_name("StartNextButton").click()
        
        return AcceptInfoPage(self.driver,self.choose_date,self.timeslot,self.office,\
                              self.first_name,self.last_name,self.emailaddress,self.phone)
    
