from selenium import webdriver

class Google_It():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def Google_Jarvis(self,query):
        self.query = query
        self.driver.get("https://www.google.com")
        search = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]')
        enter.click()


#bot = Google_It()
#bot.Google_Jarvis("modern combat ")