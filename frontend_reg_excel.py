from selenium import webdriver
import xlrd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://198-s12.nopaperforms.in/")
driver.maximize_window()
Name = "//input[@id=\"Name\"]"
Email = "//input[@id=\"Email\"]"
Mobile = "//input[@id=\"Mobile\"]"
University = "//select[@id=\"UniversityId\"]"
#universityid ="//option[@value=\"345366\"]"
Course = "//select[@id=\"CourseId\"]"
#Courseid = "//option[@value=\"345380\"]"
Specialization = "//select[@id=\"SpecializationId\"]"
#Specializationid= "//option[@value=\"345432\"]"
State= "//select[@id=\"StateId\"]"
#Stateid="//option[@value=\"26909\"]"
City="//select[@id=\"CityId\"]"
#cityid="//option[@value=\"26911\"]"
Agree="//input[@id=\"Agree\"]"
regbtn="//button[@id=\"registerBtn\"]"


class Frontend_excel:

    def Name(self, name):
        #print(name,"===> name.....")
        driver.find_element(By.ID, 'Name').clear()
        driver.find_element(By.ID, 'Name').send_keys(name)

    def Email(self, emailid):
        driver.find_element(By.ID, 'Email').clear()
        driver.find_element(By.ID, 'Email').send_keys(emailid)

    def Mobile(self,mobileno):
        driver.find_element_by_xpath(Mobile).clear()
        driver.find_element_by_xpath(Mobile).send_keys(mobileno)

    def University(self,university):
        Discipline = Select(driver.find_element_by_xpath(University))
        Discipline.select_by_visible_text(university)
        time.sleep(1)

    def Course(self,course):
        Programme = Select(driver.find_element_by_xpath(Course))
        Programme.select_by_visible_text(course)
        time.sleep(1)

    def Specialization(self,specialization):
        Subject = Select(driver.find_element_by_xpath(Specialization))
        Subject.select_by_visible_text(specialization)
        time.sleep(1)

    def State(self,state):
        State_name = Select(driver.find_element_by_xpath(State))
        State_name.select_by_visible_text(state)
        time.sleep(1)

    def City(self,city):
        City_name = Select(driver.find_element_by_xpath(City))
        City_name.select_by_visible_text(city)
        time.sleep(1)

    def agree(self):
        driver.find_element_by_xpath(Agree).click()

    def regbtn(self):
        driver.find_element_by_xpath(regbtn).click()

    def refresh(self):
        driver.refresh()
