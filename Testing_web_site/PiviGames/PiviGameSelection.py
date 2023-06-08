from selenium.webdriver.common.by import By
import Testing_web_site.constants as const
from  selenium.webdriver.common.keys import Keys

from Testing_web_site.Config_proyect import Config


class PiviGamesSelection(Config):
    def __init__(self, path_driver=r"D:\SeleniumDrivers\operadriver_win64"):
        super(PiviGamesSelection,self).__init__(path_driver,base_url=const.BASE_URL_PIVI,class_name=PiviGamesSelection)

    def Game_Searched(self, by=By.CSS_SELECTOR, path="gp-search-bar",Game="naruto",Key=Keys.ENTER):
        self.writeIn(by=by,path_name=f'{path}',value=f'{Game.join(Key)}')



    def Select_by_css(self,by= By.CSS_SELECTOR,css=''):
        btn= self.find_element(by,css)
        btn.click()





