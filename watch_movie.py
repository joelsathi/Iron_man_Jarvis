from selenium import webdriver

class watch_movie():
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    def movie_search(self):
        self.driver.get("https://www.imdb.com/chart/moviemeter/?ref=nv_nv_mpm")
        #select = self.driver.find_element_by_xpath('//*[@id="lister-sort-by-options"]')
        #select.click()
        
#bot = movie()
#bot.movie_search()