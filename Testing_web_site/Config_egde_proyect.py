import os
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Clase de configuracion para todos los tests Chrome.


class Config(webdriver.Edge):

    def __init__(self, path_driver="", teardown=False, base_url=""):
        self.path_driver = path_driver
        self.teardown = teardown
        self.base_url = base_url
        os.environ['PATH'] = self.path_driver

        super(Config, self).__init__()

        # Se llama solo en el constructor
        self.implicitly_wait(10)

        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    # Open the url. Must start all the test.
    def open(self):
        self.get(self.base_url)

    # Select the related element.
    def click_to(self, by=By.ID, path_name=""):
        id_selected = self.find_element(by, path_name)
        id_selected.click()

    def write_in(self, by=By.ID, path_name="", value=""):
        element_by = self.find_element(by, path_name)
        element_by.clear()
        element_by.send_keys(value)

    def add_key(self, by=By.ID, ref="", key=Keys.ENTER):
        element_by = self.find_element(by, ref)
        element_by.send_keys(key)
