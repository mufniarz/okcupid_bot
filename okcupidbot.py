from selenium import webdriver
import time
from secrets import username, password, intro_message

class okcupidbot:
    def __init__(self):
        print('WAITING FOR BROWSER PROCESS TO COMPLETE...')
        self.driver = webdriver.Chrome()
        self.driver.get('http://okcupid.com')
        time.sleep(15)
        self.login()

    def login(self):
        print('LOGGING YOU IN...')
        self.driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="main_content"]/div/div/div[1]/div[2]/a').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="OkModal"]/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/form/div[2]/input').click()
        time.sleep(10)
        print('LOGIN IS SUCCESSFULL, STARTING SENDING INTROS...')
        self.start_intro()
        
    def start_intro(self):
        try:
            for i in range(1, 100 + 1):
                person_name = self.driver.find_element_by_xpath('//*[@id="main_content"]/div[3]/div/div[1]/div/div/div/div/div[1]/div[1]/span[1]').text
                self.driver.find_element_by_xpath('//*[@id="main_content"]/div[3]/div/div[1]/div/div/div/div/div[1]/div[1]/span[5]/a').click()
                time.sleep(10)
                self.driver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[2]/div/div/div[3]/span/div/button[2]').click()
                time.sleep(7)
                self.driver.find_element_by_xpath('//*[@id="main_content"]/div[4]/div[2]/div[2]/div/div/div/div/div/div/div[2]/textarea').send_keys('Hey ' + person_name + intro_message)
                self.driver.find_element_by_xpath('//*[@id="main_content"]/div[4]/div[2]/div[2]/div/div/div/div/div/div/div[3]/button').click()
                time.sleep(5)
                self.driver.find_element_by_xpath('//*[@id="main_content"]/div[4]/div[2]/div[2]/div/div/div/div/div/div/div[1]/button').click()
                time.sleep(5)
                self.driver.find_element_by_xpath('//*[@id="navigation"]/div/span[1]/a[1]').click()
                time.sleep(5)
                self.driver.refresh()
                time.sleep(10)
                print('SENT INTRO TO -', person_name)

            user_response = input().lower()
            if user_response == 'y':
                self.start_intro()
            else:
                print('INVALID RESPONSE')
        except:
            print('ERROR ENCOUNTERED, RESTARTING INTRO FUNCTION')
            self.driver.get('http://okcupid.com')
            time.sleep(10)
            self.start_intro()

obj = okcupidbot()
