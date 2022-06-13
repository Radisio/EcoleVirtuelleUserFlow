# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import keyboard
from selenium.webdriver.edge.options import Options

TEST = 0
STEP_BY_STEP = 1
TEST_HEADLESS=2
mode = TEST


def wait():
    global mode
    if mode == TEST:
        return
    else:
        print("Press \"m\" to continue")
        while True:
            try:
                if keyboard.is_pressed('m'):
                    break
            except:
                break

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #Get credentials
    file = open("resources/credentials","r")
    username = file.readline()
    password = file.readline()
    option = Options()
    if mode == TEST_HEADLESS:
        option.headless=True
    driver = webdriver.ChromiumEdge(options=option)
    driver.get("https://ecolevirtuelle.provincedeliege.be")
    driver.set_window_size(1920, 1080)
    # Connection
    print("Connection...")
    try:
        username_field = driver.find_element(by=By.ID, value="userNameInput")
        username_field.send_keys(username)
        password_field = driver.find_element(by=By.ID, value="passwordInput")
        password_field.send_keys(password)
        form_authentication = driver.find_element(by=By.ID, value="formsAuthenticationArea")
        form_authentication.submit()
    except:
        print("Exception during Connection")
        assert False
    expected_url= "https://ecolevirtuelle.provincedeliege.be/myecov/ecov.accueil_gestion.Accueil"
    if driver.current_url != expected_url:
        print("Error during Connection")
        assert False
    else:
        assert True
    wait()

    print("Current url : " + driver.current_url)
    print("Go to \"Services en ligne\"")

    #Go to "Services en Ligne"
    expected_url = "https://ecolevirtuelle.provincedeliege.be/gihepnet/gihepnet_psg.eadmin_gestion.pageAccueil"
    try:
        menu = driver.find_element(by=By.ID, value="menu-secondaire")
        element_menu = menu.find_elements(by=By.TAG_NAME, value="li")
        for item in element_menu:
            if item.text == 'Services en ligne':
                item.click()
                break
    except:
        print("Exception during \"Go to 'Services en ligne'\"")
        assert False
    wait()
    print("Current url : " + driver.current_url)
    print("Change tab")
    #Change tab
    tab_list = driver.current_window_handle
    chw = driver.window_handles
    if chw.__len__()!=2:
        print("Error during \"Go to 'Services en ligne'\" : tab not created")
        assert False
    else:
        assert True
    driver.switch_to.window(chw[1])
    if driver.current_url != expected_url:
        print("Error during  \"Go to 'Services en ligne'\"")
        assert False
    else:
        assert True
    wait()
    print("Current url : " + driver.current_url)
    print("Go to \"e-Cursus\"")
    #Go to "e-Cursus"
    try:
        menu = driver.find_element(by=By.ID, value="menu")
        element_menu = menu.find_elements(by=By.TAG_NAME, value="li")
        for item in element_menu:
            if item.text == 'e-Cursus':
                item.click()
                break
    except:
        print("Error during  \"Go to 'e-Cursus'\"")
        assert False
    #Check
    try:
        menu = driver.find_element(by=By.ID, value="MainPage")
        h2_name = menu.find_element(by=By.TAG_NAME, value="h2")
        if h2_name.text != "e-Cursus":
            print("Error during \"Go to 'e-Cursus'\" ")
            assert False
        else:
            assert True
    except:
        print("Error during \"Go to 'e-Cursus'\" : h2 eCursus not found")
        assert False
    wait()
    print("Current url : " + driver.current_url)
    print("Go to \"Programme annuel de l'étudiant\"")
    #Go to "Programme annuel de l'étudiant"
    try:
        menu = driver.find_element(by=By.ID, value="idLiensTabs")
        element_menu = menu.find_elements(by=By.TAG_NAME, value="li")
        for item in element_menu:
            if item.text == 'Programme annuel de l\'étudiant':
                item.click()
                break
    except:
        print("Error during \"Go to 'Programme annuel de l'étudiant'\" ")
        assert False
    #Check
    div_BPAE = driver.find_element(by=By.ID, value="BPAE")
    class_div_BPAE = div_BPAE.get_attribute("class")
    if class_div_BPAE!="tab-pane active":
        print("Error during \"Go to 'Programme annuel de l'étudiant\"")
        assert False
    assert True
    print("No error detected")
    wait()
    driver.quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
