from selenium import webdriver
import pyttsx3 as p

class info():
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def get_info(self,query):
        self.query = query
        self.driver.get(url = "https://www.wikipedia.org/")
        search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        
        enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button/i')
        enter.click()
        
        # The definition the bot can read
        info = self.driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/p[3]')
        readable_text = info.text
        engine = p.init()
        engine.say(readable_text)
        engine.runAndWait()
        
        
# bot = info()
# bot.get_info("Srilanka")