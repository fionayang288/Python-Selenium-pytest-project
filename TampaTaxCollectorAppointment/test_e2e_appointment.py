# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 14:57:07 2020

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

class TestAppointment(BaseClass):
            
    def test_e2e_appointment(self,getData):
        log=self.getLogger()
        log.info("Below is to make an appointment at " + getData["timeslot"])
        
        homePage=HomePage(self.driver,getData["service"],getData["choose_date"],\
                          getData["timeslot"],getData["office"],getData["first_name"],\
                          getData["last_name"],getData["emailaddress"],getData["phone"])
        acceptInfoPage=homePage.selectService()
       
        #accept the information and go to next page
        appointdetailpage=acceptInfoPage.acceptInfo()
        
        #select office
        appointdetailpage.selectOffice()
        #select Date on the page
        appointdetailpage.clickCertainDate()
        try:
            namepage=appointdetailpage.selectCertainTime()
        except:
            log.warning("No available times could be found for "+getData["timeslot"])
            log.warning("try another time slot")
            return 0
        #fill in name page
        contactpage=namepage.fillName()
        
        #fill in contact page
        contactinfo=contactpage.fillContactInfo()
        contactinfo.click()
        
        #confirm info page
        assert 'Confirm appointment' == self.driver.find_element_by_class_name("header").text
        log.info("Information filled in and you can click confirm booking to make an appointment")
        print("you can click confirm booking and made your appointment now")
        #appointment confirmation
        #will not use this to submit, so this pageclass is not built, please submit/confirm it mannually
    @pytest.mark.skip
    def test_close_driver(self):
        self.driver.close()
        
#if __name__=="__main__":
#    TestAppointment().test_e2e_appointment()
    