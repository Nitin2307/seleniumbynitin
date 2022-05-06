from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import string
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://198-s12.nopaperforms.in/")
driver.maximize_window()
Name = "//input[@id=\"Name\"]"
Email = "//input[@id=\"Email\"]"
Mobile = "//input[@id=\"Mobile\"]"
University = "//select[@id=\"UniversityId\"]"
universityid ="//option[@value=\"345366\"]"
Course = "//select[@id=\"CourseId\"]"
Courseid = "//option[@value=\"345380\"]"
Specialization = "//select[@id=\"SpecializationId\"]"
Specializationid= "//option[@value=\"345432\"]"
State= "//select[@id=\"StateId\"]"
Stateid="//option[@value=\"26909\"]"
city="//select[@id=\"CityId\"]"
cityid="//option[@value=\"26911\"]"
Agree="//input[@id=\"Agree\"]"
regbtn="//button[@id=\"registerBtn\"]"

class Frontend:

    def Name(self):
        def random_name(name):
            return ''.join(random.choice(string.ascii_lowercase) for _ in range(name))
        driver.find_element(By.ID, 'Name').clear()
        driver.find_element(By.ID, 'Name').send_keys(random_name(5) +" "+ random_name(4))

    def Email(self):
        def random_email(email):
            return ''.join(random.choice(string.ascii_letters) for _ in range(email))
        driver.find_element(By.ID, 'Email').clear()
        driver.find_element(By.ID, 'Email').send_keys(random_email(8)+"@yopmail.com")

    def Mobile(self):
        driver.find_element_by_xpath(Mobile).clear()
        driver.find_element_by_xpath(Mobile).send_keys("769093388")

    def University(self):
        driver.find_element_by_xpath(University).click()
        driver.find_element_by_xpath(universityid).click()

    def Course(self):
        driver.find_element_by_xpath(Course).click()
        driver.find_element_by_xpath(Courseid).click()

    def Specialization(self):
        driver.find_element_by_xpath(Specialization).click()
        driver.find_element_by_xpath(Specializationid).click()

    def state(self):
        driver.find_element_by_xpath(State).click()
        driver.find_element_by_xpath(Stateid).click()

    def City(self):
        driver.find_element_by_xpath(city).click()
        driver.find_element_by_xpath(cityid).click()

    def agree(self):
        driver.find_element_by_xpath(Agree).click()

    def regbtn(self):
        driver.find_element_by_xpath(regbtn).click()




