from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time

class Whatsapp():
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    def Whatsapp_message(self,name,message):
        self.message = message
        self.name = name
        self.driver.get('https://web.whatsapp.com')
        wait = WebDriverWait(self.driver,600)
        time.sleep(10)
        
        target = name
        string = message
        
        #This is to locate the name which we are willing to send 
        x_arg = '//span[contains(@title,' + target + ')]'
        group_title = wait.until(EC.presence_of_element_located(( By.XPATH, x_arg )))
        group_title.click()
        message = self.driver.find_element("xpath", '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]

        for m in range(100):
            message.send_keys(string)
            sendbutton = self.driver.find_element("xpath", '//*[@id="main"]/footer/div[1]/div[3]/button')[0]
            sendbutton.click()
        

        
bot = Whatsapp()
bot.Whatsapp_message('"Aathavan"', "This is my assistance Jarvis!")