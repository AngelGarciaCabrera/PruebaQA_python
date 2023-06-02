from selenium.webdriver.common.by import By
from Testing_web_site.Config_proyect import Config
import Testing_web_site.constants as const

# Pruebas para seleccion de codigo en Codewars
class CodewarsSelection(Config):

    def __init__(self, path_driver=r"D:\SeleniumDrivers\operadriver_win64"):
        super(CodewarsSelection, self).__init__(path_driver, base_url=const.BASE_URL_CODEWARS, class_name=CodewarsSelection)

    # Seleccionar una prueba de codigo beta
    def choose_pruebas(self, tipo_prueba="beta_workout"):
        self.click_to(By.ID, "trainer_strategy")
        self.click_to(By.XPATH, f'//dd[data-strategy="{tipo_prueba}"]')

    # Seleccionar lenguaje de programacion.
    def choose_programming_language(self, language="javascript"):
        self.click_to(By.ID, "trainer_language")
        self.click_to(By.XPATH, f'//dd[data-language="{language}')

    def go_login(self):
        self.click_to(path_name="login-btn")


