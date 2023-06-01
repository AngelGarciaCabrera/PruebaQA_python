import os
from selenium import webdriver
from selenium.webdriver.common.by import By

import Carro.constants as const
from selenium.webdriver.chrome.options import Options

class Login(webdriver.Chrome):
    def __init__(self, driverPath=r"D:\SeleniumDrivers\operadriver_win64",
                 teardown=False):
        self.driverPath = driverPath
        self.teardown = teardown
        os.environ['PATH'] = self.driverPath

        chr_options = Options()
        chr_options.add_experimental_option("detach", True)
        super(Login, self).__init__(options=chr_options)

        self.implicitly_wait(20)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def open_login(self):
        self.get(const.BASE_URL)

    def click_to(self,by = By.ID, id=""):
        id_selected = self.find_element(by, id)
        id_selected.click()

    def OnlyClick(self,by = By.ID,id=""):
        id_want_to_click = self.find_element(by,id)


    def writeIn(self, by=By.ID, name="", value=""):
        element_by = self.find_element(by, name)
        element_by.clear()
        element_by.send_keys(value)
    def select_by_css(self,by= By.CSS_SELECTOR,css=''):
        btn = self.find_element(by,css)
        btn.click()

    def select_element_by_xpath (self,path=''):
        btn = self.find_element(By.XPATH,path)
        btn.click()






