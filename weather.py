from selenium import webdriver
import time

class weather():
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    def weather(self,name):
        self.driver.get("https://www.google.com")
        search = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
        search.click()
        search.send_keys("accuweather "+name)
        enter = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]')
        enter.click()
        time.sleep(2)
        
        search_weather = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/a/h3')
        search_weather.click()
        
        
# bot = weather()
# bot.weather("Batticaloa")
