# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 14:52:53 2020

@author: fiona
"""

import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from TestData.InputData import InputData
'''
def pytest_addoption(parser):
    parser.addoption(
            "--brower_name",action="store",default="chrome"
            )
#cmd line:
#py.test --brower_name firefox
#retrieve: request.config.getoption("browser_name")
'''

@pytest.fixture(scope="class")
def setup(request):
    #invoke Chrome brower
    driverpath=r"C:\Users\fiona\Documents\udemy\selenium_auto_testing\chromedriver_win32\chromedriver.exe"
    driver=webdriver.Chrome(driverpath)

    tampa_tax_collector_url="https://nqa4.nemoqappointment.com/Booking/Booking/Index/ksu3ldjsj4ks"
    driver.get(tampa_tax_collector_url)
    driver.maximize_window()
    
    request.cls.driver=driver #assign local driver to class driver
    
    yield
    
    #driver.close()


@pytest.fixture()    
def getData():
    return InputData.test_data[0]

# it will take screenshot when test failed
#@pytest.mark.hookwrapper
#def pytest_runtest_makereport(item):
#    """
#        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
#        :param item:
#        """
#    pytest_html = item.config.pluginmanager.getplugin('html')
#    outcome = yield
#    report = outcome.get_result()
#    extra = getattr(report, 'extra', [])
#
#    if report.when == 'call' or report.when == "setup":
#        xfail = hasattr(report, 'wasxfail')
#        if (report.skipped and xfail) or (report.failed and not xfail):
#            file_name = report.nodeid.replace("::", "_") + ".png"
#            _capture_screenshot(file_name)
#            if file_name:
#                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                extra.append(pytest_html.extras.html(html))
#        report.extra = extra
#
#
#def _capture_screenshot(name):
#        driver.get_screenshot_as_file(name)
