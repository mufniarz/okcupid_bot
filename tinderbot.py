from selenium import webdriver
from time import sleep

class tinderbot:
  def __init__(self):
    print('WAITING FOR BROWSER PROCESS TO COMPLETE...')
    self.driver = webdriver.Chrome()
    self.driver.get('http://tinder.com')
    sleep(10)
    # self.login()

  def login(self):
    print('LOGGING YOU IN...')
    self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button').click()
    sleep(2)
    self.driver.find_element(By.link  )
    sleep(2)
    self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[2]/div/input').send_keys('9417006030')
    self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button').click()
    print('ENTER OTP SENT TO YOUR PHONE TO LOGIN...')
    otp = input()
    self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[3]/input[1]').send_keys(otp[0])
    self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[3]/input[2]').send_keys(otp[1])
    self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[3]/input[3]').send_keys(otp[2])
    self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[3]/input[4]').send_keys(otp[3])
    self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[3]/input[5]').send_keys(otp[4])
    self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[3]/input[6]').send_keys(otp[5])
    self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button').click()
    sleep(5)

  def start_swiping(self):
    print('HOW MANY PEOPEL TO SWIPE-->')
    number_of_swipes = int(input())
    for i in range(1, number_of_swipes + 1):
      self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button').click()
      sleep(1)

    print('ALL ' + str(number_of_swipes) + ' SWIPED SUCCESSFULLY DO YOU WISH TO SWIPE MORE TYPE (y)ES OR (n)O:')
    user_response = input().lower()
    if user_response == 'y':
        self.start_swiping()
    else:
        print('INVALID RESPONSE')

obj = tinderbot()
