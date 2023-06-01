
from Testing_web_site.codewars.CodewarsSelection import CodewarsSelection

with CodewarsSelection() as tester:
    tester.open()

    tester.go_login()
    tester.writeIn(path_name="user_email", value="Hola")
    tester.writeIn(path_name="user_password", value="Hola")

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
    # #we try to add a foro but may be we can't
    #
    # #then we try to moved to other page
    #
    # #with css selector we can pass other params what different class
    # tester.select_by_css(css='a[data-toggle="collapse"]')
    # #then we go to add text into the foro
    # tester.writeIn(By.ID,"id_subject","añandiendo un foro desde QA..")
    # tester.writeIn(By.ID,'id_messageeditable',"el loco en añadidera de foro automatico no bulto ni paquete")








