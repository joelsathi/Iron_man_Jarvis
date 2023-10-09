from selenium import webdriver

class music():
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def music(self,name):
        self.name = name
        self.driver.get('https://www.youtube.com/results?search_query='+name)
        video = self.driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
        video.click()
        
#bot = music()
#bot.music("Who am I by casting crowns")

