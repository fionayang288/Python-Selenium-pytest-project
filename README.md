# Python-Selenium-pytest-project

### Object
This project is to automatically find available timeslots for services on Tampa Hillsborough County Tax Collector appointment website <https://nqa4.nemoqappointment.com/Booking/Booking/Index/ksu3ldjsj4ks>, and automatically fill in all appointment information and bring you to confirm booking page

### User Guidance
To use this project, you need to follow below steps:

1. Download selenium webdriver for the brower you use from <https://www.selenium.dev/downloads/> (I download the chrome one)
2. Set "driverpath" in file Python-Selenium-pytest-project/TampaTaxCollectorAppointment/conftest.py (my driverpath=r"C:\Users\fiona\Documents\udemy\selenium_auto_testing\chromedriver_win32\chromedriver.exe")
3. Set "service", "office", personal information etc. in file Python-Selenium-pytest-project/TestData/InputData.py
4. Open cmd and go to this Python-Selenium-pytet-project folder, enter command "py.test"

You should be able to see two websites opened, one with available timeslots shown, the other on review page so that you can click "confirm booking".
You can also see all available timeslots in the logfile.log file 
