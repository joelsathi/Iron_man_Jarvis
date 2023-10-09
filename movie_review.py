from selenium import webdriver

class movie():
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    def get_review(self,name):
        self.driver.get("https://www.google.com")
        search = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
        search.click()
        search.send_keys(name + " reviews")
        enter = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]')
        enter.click()
        
#bot = movie()
#bot.get_review("Toy story 4")

