import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# Clase de configuracion para todos los tests.
class Config(webdriver.Chrome):

    def __init__(self, path_user="",
                 teardowm=False, base_url="", class_name=None):
        self.PathUser = path_user
        self.teardowm = teardowm
        self.base_url = base_url
        os.environ['PATH'] = self.PathUser

        # Ojo despues
        # self.chr_options = class_for_config_chrome()
        # super(Config, self).__init__(option=self.chr_options)
        chr_options = Options()
        chr_options.add_experimental_option("detach", True)
        super(Config, self).__init__(options=chr_options)

        # Se llama solo en el constructor
        self.implicitly_wait(10)

        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardowm:
            self.quit()

    def open(self):
        self.get(self.base_url)

    # METHOD FOR USE
    def click_to(self, by=By.ID, path_name=""):
        id_selected = self.find_element(by, path_name)
        id_selected.click()

    def writeIn(self, by=By.ID, path_name="", value=""):
        element_by = self.find_element(by, path_name)
        element_by.clear()
        element_by.send_keys(value)
    def addTextToKey(self,by=By.ID,Key=""):
        element_by = self.find_element(by,Key)
        element_by.send_keys(Key)
