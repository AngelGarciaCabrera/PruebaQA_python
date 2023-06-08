# this test check use of the codewars with selenium.
from selenium.webdriver.common.by import By

from Testing_web_site.codewars.edge.CodewarsSelectionEdge import CodewarsSelection

USERNAME = "Elioerickramos@gmail.com"
PASSWORD = "Mosquea42510"

with CodewarsSelection() as tester:
    tester.open()

    # Go to Log in
    tester.go_login()

    # Go to GitHub log in
    tester.click_to(By.XPATH, '//form[@id="new_user"]/button[1]')

    # Add credentials to GitHub
    tester.write_in(path_name="login_field", value=USERNAME)
    tester.write_in(path_name="password", value=PASSWORD)
    tester.click_to(By.XPATH, '//form/div/input[13]')

    # Choose a code test

    tester.choose_pruebas()
    tester.choose_programming_language()
