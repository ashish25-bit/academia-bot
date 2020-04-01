from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
import datetime
import math

class academia():
    def __init__(self):
        self.driver = webdriver.Chrome()

    # to check whether the element is present
    def findElement(self,xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True


    def login(self):
        url = 'https://academia.srmist.edu.in/accounts/signin?_sh=false&hideidp=true&portal=10002227248&client_portal=true&servicename=ZohoCreator&service_language=en&serviceurl=https%3A%2F%2Facademia.srmist.edu.in%2F'
        self.driver.get(url)
        sleep(2)
        username = input('Enter your username\n')
        password = input('Enter password\n')
        print()
        email = self.driver.find_element_by_xpath('//*[@id="Email"]')
        email.send_keys(username)
        passF = self.driver.find_element_by_xpath('//*[@id="Password"]')
        passF.send_keys(password)
        btn = self.driver.find_element_by_xpath('//*[@id="signinForm"]/div[5]/input')
        btn.click()
        sleep(5)
        
        # get to the attendance
        attendande_link = 'https://academia.srmuniv.ac.in/#View:My_Attendance'
        self.driver.get(attendande_link)
        sleep(5)

        # to handle the error
        if(self.findElement('//*[@id="details-button"]')):
            advance_btn = self.driver.find_element_by_xpath('//*[@id="details-button"]')
            advance_btn.click()
            proceed = self.driver.find_element_by_xpath('//*[@id="proceed-link"]')
            proceed.click()
            sleep(5)
        
        parent = self.driver.find_element_by_xpath('//*[@id="zc-viewcontainer_My_Attendance"]/div[1]/div[4]/div/table[2]/tbody')
        child = parent.find_elements_by_xpath('//*[@id="zc-viewcontainer_My_Attendance"]/div[1]/div[4]/div/table[2]/tbody/tr')
        courseCode = []
        subject = []
        category = []
        hoursConducted = []
        hoursAbsent = []
        attendandePercentage = []
        
        for i in range (2,len(child)+1):
            cc   = self.driver.find_element_by_xpath('//*[@id="zc-viewcontainer_My_Attendance"]/div[1]/div[4]/div/table[2]/tbody/tr['+str(i)+']/td[1]')
            s    = self.driver.find_element_by_xpath('//*[@id="zc-viewcontainer_My_Attendance"]/div[1]/div[4]/div/table[2]/tbody/tr['+str(i)+']/td[2]')
            cate = self.driver.find_element_by_xpath('//*[@id="zc-viewcontainer_My_Attendance"]/div[1]/div[4]/div/table[2]/tbody/tr['+str(i)+']/td[3]')
            hc   = self.driver.find_element_by_xpath('//*[@id="zc-viewcontainer_My_Attendance"]/div[1]/div[4]/div/table[2]/tbody/tr['+str(i)+']/td[7]')
            ha   = self.driver.find_element_by_xpath('//*[@id="zc-viewcontainer_My_Attendance"]/div[1]/div[4]/div/table[2]/tbody/tr['+str(i)+']/td[8]')
            ap   = self.driver.find_element_by_xpath('//*[@id="zc-viewcontainer_My_Attendance"]/div[1]/div[4]/div/table[2]/tbody/tr['+str(i)+']/td[9]')

            index = cc.text.index("\nRegular")
            cct = cc.text[:index]

            courseCode.append(cct)
            subject.append(s.text)
            category.append(cate.text)
            hoursConducted.append(hc.text)
            hoursAbsent.append(ha.text)
            attendandePercentage.append(ap.text)
        
        for j in range(len(subject)):
            canBunk = 0
            if(float(attendandePercentage[j]) >= 75):
                fh = math.floor( ( (int(hoursConducted[j]) - int(hoursAbsent[j]) ) *100 )/75)
                if(fh > int(hoursConducted[j])):
                    canBunk = fh-int(hoursConducted[j])         
            print(subject[j] + ' (' + category[j] + ') - Can Bunk = ' + str(canBunk))
            print()

        logoutBtn = self.driver.find_element_by_xpath('//*[@id="zc-header-right"]/table/tbody/tr/td[4]/a')
        logoutBtn.click()


bot = academia()
bot.login()