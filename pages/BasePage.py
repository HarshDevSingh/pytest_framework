class BasePage:
    def __int__(self,driver,route_url=""):
        self.driver=driver
        self.base_url="https://www.saucedemo.com/"

    def open(self):
        self.driver.get(self.base_url)