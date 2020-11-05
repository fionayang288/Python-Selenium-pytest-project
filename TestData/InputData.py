# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 23:52:28 2020

@author: fiona
"""

'''
service option:
    "Birth Certificates"
    "Business Tax"
    "Concealed Permit"
    "Dealerships  "
    "Driver License and ID Cards"
    "HazMat"
    "Hunting and Fishing"
    "Parking Permit"
    "Property Tax"
    "Registration"
    "Road Test"
    "Titles"
    "Vehicle for Hire"
    "Written Test"

office option:
    "Brandon Branch - 3030 North Falkenburg Road, Tampa"
    "Drew Park Branch, 4100 West Martin Luther King. Jr. Blvd, Tampa"
    "East Tampa Branch, 2814 E Hillsborough Ave, Tampa"
    "North Tampa Branch, 3011 University Center Dr., Suite 150, Tampa"
    "Plant City Branch, 1834 James Redman Parkway (SR 39), Plant City"
    "Southshore Branch, 406 30th Street S.E., Ruskin"
    
'''
from datetime import datetime

class InputData:
    test_data=[{
        "service":"Driver License and ID Cards", #options listed above
        "first_name":"fiona",
        "last_name":"yang",
        "emailaddress":"fiona.yang28@gmail.com",
        "phone":"6468306049",
         "office":"East Tampa Branch, 2814 E Hillsborough Ave, Tampa", #options listed above
         "choose_date":datetime(2020,12,3),
         "timeslot":'12/3/2020 3:00:00 PM'
        }]
    