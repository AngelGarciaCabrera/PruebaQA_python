
# from Testing_web_site.codewars.CodewarsSelection import CodewarsSelection
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Testing_web_site.PiviGames.PiviGameSelection import PiviGamesSelection

with PiviGamesSelection() as tester:
    tester.open()
    tester.click_to(by=By.ID,path_name="onesignal-slidedown-cancel-button")
    tester.click_to(by=By.ID, path_name="gp-search-button")
    tester.writeIn(by=By.CSS_SELECTOR, path_name='input[placeholder="search"]', value="naruto")
    tester.Game_Searched(by=By.CSS_SELECTOR, path='input[placeholder="search"]', Game="naruto", Key=Keys.ENTER)
    tester.click_to(by=By.XPATH, path_name='//h2/a[@title="NARUTO SHIPPUDEN ULTIMATE NINJA STORM 4 ROAD TO BORUTO Next'
                                            ' Generation+ ONLINE STEAM v2 + Update 1.09"]')
    tester.focus_in_elemet(By.XPATH, '//*[@id="movie_player"]/div[4]/button')
    tester.click_to(by=By.XPATH, path_name='//*[@id="movie_player"]/div[4]/button')


    # tester.choose_pruebas()
    # tester.choose_programming_language()


# with Login() as tester:
    # tester.open_login()
    # tester.writeIn(By.CSS_SELECTOR,
    #                "username",
    #                "20210306")
    #
    # tester.writeIn(By.ID, "password", "Angel11neutroblack.")
    # tester.click_to(path_name="loginbtn")
    #
    # #NEXT TEST, this test is in the "plataforma Virtual", there we try to check the section of class
    # tester.select_by_css(css='a[class="dropdown-toggle nav-link"]')
    # tester.select_by_css(css='a[title="2023-C-2-1615-2880-TDS-007"]')
    #
    # #then we try to add text on the foro
    # tester.select_element_by_xpath("//span[@class='instancename' and text()='Foro de presentación']")
    #
    # #we try to add a forobut maybe we can't
    #
    # #then we try tomoved to other page
    #
    # #with css selector we can pass other params what different class
    # tester.select_by_css(css='a[data-toggle="collapse"]')
    # #then we go to add text into the foro
    # tester.writeIn(By.ID,"id_subject","añandiendo un foro desde QA..")
    # tester.writeIn(By.ID,'id_messageeditable',"el loco en añadidera de foro automatico no bulto ni paquete")








