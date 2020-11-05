# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 19:22:42 2020

@author: fiona
"""

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from utilities.BaseClass import BaseClass

from pageObjects.HomePage import HomePage

class TestShowTimeSlot(BaseClass):    
    timeoption="selectCertain"
    #selectCertain
    #selectFirstAvailable
    
    def test_show_timeslot(self,getData):
        log=self.getLogger()
        
        homePage=HomePage(self.driver,getData["service"],getData["choose_date"],\
                          getData["timeslot"],getData["office"],getData["first_name"],\
                          getData["last_name"],getData["emailaddress"],getData["phone"])
        acceptInfoPage=homePage.selectService()
        
        #accept the information and go to next page
        appointdetailpage=acceptInfoPage.acceptInfo()
        
        #select office
        appointdetailpage.selectOffice()
        #select Date on the page
        if TestShowTimeSlot.timeoption=="selectCertain":
            log.info("select " +datetime.strftime(getData['choose_date'],"%m/%#d/%Y")+" for available timeslots")
            appointdetailpage.clickCertainDate()
            try:
                msgnotavailable=self.driver.find_element_by_xpath("//label[@style='color:Red;']").text
                #assert "No available times" in msgnotavailable
                log.info("No available times could be found for "+datetime.strftime(getData['choose_date'],"%m/%#d/%Y"))
                return print('No available times could be found.')
            except NoSuchElementException:
                pass
            availability=appointdetailpage.showAllAvailableTimeforCertainDate()
            log.info("Available timeslots found for "+datetime.strftime(getData['choose_date'],"%m/%#d/%Y"))
            log.info(availability)
            log.info("earliest time slot available is "+availability[0])
            return availability
        
        elif TestShowTimeSlot.timeoption=="selectFirstAvailable":
            log.info("select first available date for available timeslots")
            appointdetailpage.clickFirstAvailableTimes()
            try:
                msgnotavailable=self.driver.find_element_by_xpath("//label[@style='color:Red;']").text
                #assert "No available times" in msgnotavailable
                log.info("No available times could be found at all")
                return print('No available times could be found.')
            except NoSuchElementException:
                log.info("Available timeslots found for first available date")
                availability=appointdetailpage.showAllAvailableTimeforCertainDate()
                log.info(availability)
                log.info("earliest time slot available is "+availability[0])  
                return availability

    @pytest.mark.skip
    def test_close_driver(self):
        self.driver.close()