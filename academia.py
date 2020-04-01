from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from secrets import password
from time import sleep
import datetime

class academia():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def findElement(self,xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True


    def login(self):
        url = 'https://academia.srmist.edu.in/accounts/signin?_sh=false&hideidp=true&portal=10002227248&client_portal=true&servicename=ZohoCreator&service_language=en&serviceurl=https%3A%2F%2Facademia.srmist.edu.in%2F'
        username = 'ashishyoel_ma@srmuniv.edu.in'
        self.driver.get(url)
        sleep(2)
        email = self.driver.find_element_by_xpath('//*[@id="Email"]')
        email.send_keys(username)
        passF = self.driver.find_element_by_xpath('//*[@id="Password"]')
        passF.send_keys(password)
        btn = self.driver.find_element_by_xpath('//*[@id="signinForm"]/div[5]/input')
        btn.click()
        sleep(5)
        
        

        attendande_link = 'https://academia.srmuniv.ac.in/#View:My_Attendance'
        self.driver.get(attendande_link)
        sleep(5)

        if(self.findElement('//*[@id="details-button"]')): 
            print('Advance button is there')
            advance_btn = self.driver.find_element_by_xpath('//*[@id="details-button"]')
            advance_btn.click()
            proceed = self.driver.find_element_by_xpath('//*[@id="proceed-link"]')
            proceed.click()
            self.driver.get(attendande_link)
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
            if(float(attendandePercentage[j]) >= 75 and float(attendandePercentage[j]) <= 80):
                print('Your attendance in ' + subject[j] + ' (' + category[j] + ') is less than 80%. Be cautious!!')
            elif(float(attendandePercentage[j]) > 80 and float(attendandePercentage[j]) <= 90):
                print('Your attendance in ' + subject[j] + ' (' + category[j] + ') is more than 80%. Chill!!')
            elif(float(attendandePercentage[j]) > 90 and float(attendandePercentage[j]) <= 100):
                print('Your attendance in ' + subject[j] + ' (' + category[j] + ') is more than 90%. Get Some Life Dude!!')
            else : 
                print('You are doomed!! Your attendance in ' + subject[j] + ' (' + category[j] + ') is less than 75%')
            print()

        
'''
        academic_planner = 'https://academia.srmist.edu.in/#View:Academic_Planner_2019_20_EVEN'
        d = datetime.datetime.now()
        date = d.day + 1
        month = d.strftime("%b") + " \'" +  d.strftime("%y")
        day = d.strftime("%a")

        self.driver.get(academic_planner)
        sleep(5)
        m = self.driver.find_element_by_xpath('//font[contains(text(), "' + month + '")]')
        month_index = 0
        
        for x in range (3,28,5):
            ele = self.driver.find_element_by_xpath('//*[@id="zc-viewcontainer_Academic_Planner_2019_20_EVEN"]/div[1]/table[1]/tbody/tr[1]/th['+str(x)+']/strong/font')
            if(m.text == ele.text) :
                month_index = x
                break
        
        dates = []
        dayOrder = []
        event = []
        days = [] 

        for i in range(7): 
            dd   = self.driver.find_element_by_xpath('//*[@id="zc-viewcontainer_Academic_Planner_2019_20_EVEN"]/div[1]/table[1]/tbody/tr['+str(date+i)+']/td['+str(month_index-2)+']')
            dayy = self.driver.find_element_by_xpath('//*[@id="zc-viewcontainer_Academic_Planner_2019_20_EVEN"]/div[1]/table[1]/tbody/tr['+str(date+i)+']/td['+str(month_index-1)+']')
            do   = self.driver.find_element_by_xpath('//*[@id="zc-viewcontainer_Academic_Planner_2019_20_EVEN"]/div[1]/table[1]/tbody/tr['+str(date+i)+']/td['+str(month_index+1)+']')
            dates.append(dd.text)
            days.append(dayy.text)
            dayOrder.append(do.text)

        print(dates)
        print(days)
        print(dayOrder)

'''

bot = academia()
bot.login()