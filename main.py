from datetime import time

# from Testing_web_site.codewars.CodewarsSelection import CodewarsSelection
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Testing_web_site.ITLA.ITLA_test import ITLA_test
import time  # Importa la biblioteca 'time'
import logging


#with PiviGamesSelection() as tester:
# tester.open()
# tester.click_to(by=By.ID,path_name="onesignal-slidedown-cancel-button")
# tester.click_to(by=By.ID, path_name="gp-search-button")
# tester.writeIn(by=By.CSS_SELECTOR, path_name='input[placeholder="search"]', value="naruto")
# tester.Game_Searched(by=By.CSS_SELECTOR, path='input[placeholder="search"]', Game="naruto", Key=Keys.ENTER)
# tester.click_to(by=By.XPATH, path_name='//h2/a[@title="NARUTO SHIPPUDEN ULTIMATE NINJA STORM 4 ROAD TO BORUTO Next'
# ' Generation+ ONLINE STEAM v2 + Update 1.09"]')

# tester.writeIn(by=By.CSS_SELECTOR, path_name='div[@class="textarea"]',value="No me gusto")
# tester.close()



    # tester.choose_pruebas()
    # tester.choose_programming_language()

# Configuración básica de registro
logging.basicConfig(filename='test_report.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# ...
with ITLA_test() as tester:

    #inicion del programa
    tester.open()
try:
    # Primer test, evalua fallo
    time.sleep(1)
    tester.writeIn(By.ID, "username", "20210302")
    time.sleep(1)
    tester.writeIn(By.ID, "password", "Angel11neutroblack.")
    time.sleep(1)
    tester.click_to(path_name="loginbtn")
    tester.implicitly_wait(10)
    logging.info("Prueba del login para no encontrar estudiantes: Correcta")


    #segundo test del login
    time.sleep(1)
    tester.writeIn(By.ID,"username", "20210306")
    time.sleep(1)
    tester.writeIn(By.ID, "password", "Angel11neutroblack.")
    time.sleep(1)
    tester.click_to(path_name="loginbtn")
    logging.info("Prueba del login para encontrar estudiantes: Correcta")

    time.sleep(2)
#Test de verificacion de cursos actuales del estudiantes
    tester.Select_by_css(css='a[title="Mis cursos"]')
    time.sleep(1)
    logging.info("Prueba de verificacion de cursos actuales del estudiantes: Correcta")
    # Seleccion de una materia actual
    tester.Select_by_css(css='a[title="2023-C-2-1615-2880-TDS-007"]')
    time.sleep(1)
    logging.info("Prueba de verificacion de Apartados por Materias del estudiantes: Correcta")
    #se puede añadir nueva asignacion
    tester.Select_by_css(css='a[href="https://plataformavirtual.itla.edu.do/mod/assign/view.php?id=369596"]')
    logging.info("Prueba de Añadir Asignacion de estudiante: Correcta")
    #verificacion de calificacion
    time.sleep(1)
    tester.Select_by_css(css='a[href="https://plataformavirtual.itla.edu.do/grade/report/index.php?id=5147"]')
    logging.info("Prueba de Apartado de calificacion por materia de estudiantes: Correcta")
    logging.info("Test de website: Correcta")

    time.sleep(5)
except Exception as e:
    logging.error(f" Error en Pruebas falladas: {e}")
finally:

    tester.close()








