# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 17:14:22 2020

@author: fiona
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass
from pageObjects.NamePage import NamePage

class AppointDetailPage:
       
    def __init__(self,driver,choose_date,timeslot,office,\
                 first_name,last_name,emailaddress,phone):
        self.driver=driver
        self.date=choose_date
        self.date_str=self.date.strftime("%m/%#d/%Y") #'11/3/2020'
        self.date_short=self.date.strftime("%b%d%Y") #'Nov032020'
        self.time_list=[]       
        self.timeslot=timeslot
        self.office=office
        self.first_name=first_name
        self.last_name=last_name
        self.emailaddress=emailaddress
        self.phone=phone
    
    def selectOffice(self):
        locator=self.driver.find_element_by_name("SectionId")
        BaseClass.selectOptionByText(self,locator,self.office)
    
    def clickCertainDate(self):
        
        datepicker = self.driver.find_element_by_id("FromDateString")
        datepicker.click()
        
        selectMonth = self.driver.find_element_by_xpath('//select[@class="ui-datepicker-month"]')
        for option in selectMonth.find_elements_by_tag_name('option'):
            if option.text == self.date_short[:3]:
                option.click() 
                break
        
        selectYear = self.driver.find_element_by_xpath('//select[@class="ui-datepicker-year"]')
        for option in selectYear.find_elements_by_tag_name('option'):
            if option.text == self.date_short[-4:]:
                option.click() 
                break 
        
        days = self.driver.find_elements_by_xpath('//a[@class="ui-state-default"]')
        for day in days:
            if day.text==str(int(self.date_short[3:5])):
                day.click()
                break
        #available time slots will be available on the webpage then
        
    
    def clickFirstAvailableTimes(self):
        firstAvailableButton=self.driver.find_element_by_xpath("//input[@name='TimeSearchFirstAvailableButton']")
        firstAvailableButton.click()
        
    def showAllAvailableTimeforCertainDate(self):
        self.time_list=[]
        all_labels=self.driver.find_elements_by_xpath("//div[@class='pointer timecell text-center ']")
        for label in all_labels:
            #time format 12/1/2020 8:30:00 AM, string to datetime for sorting
            self.time_list.append(datetime.strptime(label.get_attribute('aria-label'), "%m/%d/%Y %I:%M:%S %p"))
        self.time_list.sort()
        #datetime to string for presenting
        self.time_list=list(map(lambda x :datetime.strftime(x,"%#m/%#d/%Y %#I:%M:%S %p"),self.time_list))
        return self.time_list
    
    def selectCertainTime(self):
        timeslot_element1=self.driver.find_element_by_xpath("//div[@aria-label={}{}{}]/..".format("'",self.timeslot,"'"))
        timeslot_element2=self.driver.find_element_by_xpath("//div[@aria-label={}{}{}]".format("'",self.timeslot,"'"))
        self.driver.execute_script("arguments[0].setAttribute('class','cellcontainer hinted')", timeslot_element1)
        self.driver.execute_script("arguments[0].setAttribute('class','pointer timecell text-center  selected')", timeslot_element2)
        
        self.driver.find_element_by_xpath("//div[@aria-label={}{}{}]".format("'",self.timeslot,"'")).click()
        
        self.driver.find_element_by_name("Next").click()
        #this will give object to click to go to next page
        return NamePage(self.driver,self.first_name,self.last_name,self.emailaddress,self.phone)
