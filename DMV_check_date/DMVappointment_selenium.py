# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 19:16:14 2020

@author: fiona
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from datetime import datetime
from selenium.webdriver.common.by import By


driver=webdriver.Chrome(r"C:\Users\fiona\Documents\udemy\selenium_auto_testing\chromedriver_win32\chromedriver.exe")

tax_collector_url="https://nqa4.nemoqappointment.com/Booking/Booking/Index/ksu3ldjsj4ks"
driver.get(tax_collector_url)
driver.maximize_window()

print(driver.title) # hillsborough county appointments

service_group=Select(driver.find_element_by_id("ServiceGroupId"))

service_group.select_by_visible_text("Driver License and ID Cards")
'''
<select id="ServiceGroupId" name="ServiceGroupId"><option selected="selected" value="0">Please select...</option>
<option value="282">Birth Certificates</option>
<option value="111">Business Tax</option>
<option value="117">Concealed Permit</option>
<option value="278">Dealerships  </option>
<option value="113">Driver License and ID Cards</option>
<option value="115">HazMat</option>
<option value="112">Hunting and Fishing</option>
<option value="107">Parking Permit</option>
<option value="110">Property Tax</option>
<option value="108">Registration</option>
<option value="116">Road Test</option>
<option value="109">Titles</option>
<option value="279">Vehicle for Hire</option>
<option value="114">Written Test</option>
</select>
'''
#click the button: make an appointment, and then it will go to next page
driver.find_element_by_name("StartNextButton").click()
#accept the information and go to next page
driver.find_element_by_name("AcceptInformationStorage").click()
driver.find_element_by_name("Next").click()
#select Region, office, appointment queue and date
office=Select(driver.find_element_by_name("SectionId"))
office.select_by_visible_text("East Tampa Branch, 2814 E Hillsborough Ave, Tampa")
'''
<select data-function="data-provider-subscriber" data-key="sections" data-param="sectionId" data-provider="#RegionId" data-url="/Booking/Ajax/GetServiceTypes?serviceGroupId=113" id="SectionId" name="SectionId" tabindex="0"><option value="59"> Please Select...</option>
<option value="51">Brandon Branch - 3030 North Falkenburg Road, Tampa</option>
<option value="54">Drew Park Branch, 4100 West Martin Luther King. Jr. Blvd, Tampa</option>
<option value="53">East Tampa Branch, 2814 E Hillsborough Ave, Tampa</option>
<option value="55">North Tampa Branch, 3011 University Center Dr., Suite 150, Tampa</option>
<option value="56">Plant City Branch, 1834 James Redman Parkway (SR 39), Plant City</option>
<option value="57">Southshore Branch, 406 30th Street S.E., Ruskin</option>
</select>
'''
#select Date on the page
today=datetime(2020,12,2)
# use today: today=datetime.today()
# or use certain date: today=datetime(2020,12,03)

today_str=today.strftime("%m/%#d/%Y") #'11/3/2020'
today_short=today.strftime("%b%d%Y") #'Nov032020'

datepicker = driver.find_element_by_id("FromDateString")
datepicker.click()

selectMonth = driver.find_element_by_xpath('//select[@class="ui-datepicker-month"]')
for option in selectMonth.find_elements_by_tag_name('option'):
    if option.text == today_short[:3]:
        option.click() 
        break

selectYear = driver.find_element_by_xpath('//select[@class="ui-datepicker-year"]')
for option in selectYear.find_elements_by_tag_name('option'):
    if option.text == today_short[-4:]:
        option.click() 
        break 

days = driver.find_elements_by_xpath('//a[@class="ui-state-default"]')
for day in days:
    if day.text==str(int(today_short[3:5])):
        day.click()
        break

try:
    msg=driver.find_element_by_xpath("//div[@class='validation-summary-errors alert alert-error']")
    assert "Invalid date" not in msg.text
    print("good to go, print available time slots")
    '''
    timetable=driver.find_element_by_class_name("timetable").find_element_by_tag_name("tbody")
    rows = timetable.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table
    for row in rows:
        # Get the columns (all the column 2)        
        col = row.find_elements_by_tag_name("td")[2]
        print(col.text)
    '''
    time_list=[]
    all_labels=driver.find_elements_by_xpath("//div[@class='pointer timecell text-center ']")
    for label in all_labels:
        #time format 12/1/2020 8:30:00 AM
        time_list.append(datetime.strptime(label.get_attribute('aria-label'), "%m/%d/%Y %I:%M:%S %p"))
        time_list.sort()
    time_list=list(map(lambda x :datetime.strftime(x,"%#m/%#d/%Y %#I:%M:%S %p"),time_list))
    
    timeslot=time_list[3]
    timeslot_element=driver.find_element_by_xpath("//div[@aria-label={}{}{}]".format("'",timeslot,"'"))
    driver.execute_script("arguments[0].setAttribute('class','pointer timecell text-center selected')", timeslot_element)
    
    driver.find_element_by_name("Next").click()
    
    driver.find_element_by_name("Customers[0].BookingFieldValues[0].Value").send_keys("fiona")
    driver.find_element_by_name("Customers[0].BookingFieldValues[1].Value").send_keys("yang")
    nextbutton=driver.find_element_by_name("Next")
    nextbutton.click()
    
    
except:
    print("Invalid date, use first available time")
    driver.find_element_by_xpath("//input[@name='TimeSearchFirstAvailableButton']").click()
    all_labels=driver.find_elements_by_xpath("//div[@class='pointer timecell text-center ']")
    for label in all_labels:
        print(label.get_attribute('aria-label'))
#convert string to datetime
datetime.strptime(label.get_attribute('aria-label'), "%m/%d/%Y %I:%M %p")

driver.close()

