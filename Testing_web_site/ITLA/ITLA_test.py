from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
import Testing_web_site.constants as const

from Testing_web_site.Config_proyect import Config


class ITLA_test(Config):
    def __init__(self, path_driver=r"D:\SeleniumDrivers\operadriver_win64"):
        super(ITLA_test, self).__init__(path_driver, base_url=const.BASE_URL,
                                                 class_name=ITLA_test)

    def Game_Searched(self, by=By.CSS_SELECTOR, path="gp-search-bar", Game="naruto", Key=Keys.ENTER):
        self.writeIn(by=by, path_name=f'{path}', value=f'{Game}')
        self.addTextToKey(by=By.CSS_SELECTOR, path=f'{path}', Key=Key)
    def Select_by_css(self, by=By.CSS_SELECTOR, css=''):
        btn = self.find_element(by, css)
        btn.click()

    def focus_in_elemet(self,by=By.XPATH, Path=''):
        btn = self.find_element(by,Path)
        self.execute_script("arguments[0].scrollIntoView();", btn)

    def click_to(self, by=By.ID, path_name=""):
        id_selected = self.find_element(by, path_name)
        id_selected.click()

    def writeIn(self, by=By.ID, path_name="", value=""):
        element_by = self.find_element(by, path_name)
        element_by.clear()
        element_by.send_keys(value)

    def addTextToKey(self, by=By.ID, path="", Key=Keys.ENTER):
        element_by = self.find_element(by, path)
        element_by.send_keys(Key)
