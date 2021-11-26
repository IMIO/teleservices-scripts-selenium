from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
# chrome_options.add_argument("--no-sandbox")  # needed for Linux
# chrome_options.add_argument("--headless")  # needed for Linux
chrome_options.add_argument("window-size=1900,1080")
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()


def open_browser_at(url):
    driver.get(url)


def click(xpath):
    print("Clicking on element (xpath) : ", xpath)
    driver.execute_script(
        "arguments[0].click();",
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, xpath))),
    )


def click_next_button():
    driver.execute_script(
        "arguments[0].click();",
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[value="Suivant"]'))),
    )


def click_validate_button():
    driver.execute_script(
        "arguments[0].click();",
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[value="Valider"]'))),
    )


def select_option_from_dropdown_menu(id, option):
    select = Select(driver.find_element(By.ID, id))
    select.select_by_visible_text(option)


def fill_text_field_with(xpath, value):
    text_field = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    text_field.clear()
    text_field.send_keys(value)


def fill_cert_nationalite_form(
    firstname,
    lastname,
    national_id,
    birth_date,
    street,
    number,
    zipcode,
    city,
    mail,
    phone
):
    click('//*[@id="columns"]/div[1]/div/div/div/ul/li[3]/a')
    click('//*[@id="var_mode_delivrance"]/div[2]/label[2]/span')
    click_next_button()
    click('//*[@id="var_concerne_qui"]/div[2]/label[1]/span')
    click('//*[@id="var_mode_delivrance"]/div[2]/label[2]/span')
    click('//*[@id="var_rb_domicile"]/div[2]/label[1]/span')
    click('//*[@id="var_rb_domicile"]/div[2]/label[1]/span')
    click_next_button()
    fill_text_field_with('//*[@id="form_f8"]', firstname)
    fill_text_field_with('//*[@id="form_f9"]', lastname)
    fill_text_field_with('//*[@id="form_f10"]', national_id)
    fill_text_field_with('//*[@id="form_f72"]', birth_date)
    fill_text_field_with('//*[@id="form_f13"]', street)
    fill_text_field_with('//*[@id="form_f14"]', number)
    fill_text_field_with('//*[@id="form_f50"]', zipcode)
    fill_text_field_with('//*[@id="form_f70"]', city)
    select_option_from_dropdown_menu("form_f71", "Belgique")
    fill_text_field_with('//*[@id="form_f18"]', mail)
    fill_text_field_with('//*[@id="form_f19"]', phone)
    click_next_button()
    fill_text_field_with('//*[@id="form_f25"]', '01/01/2001')
    select_option_from_dropdown_menu("form_f21", "Avocat")
    select_option_from_dropdown_menu("form_f33", "Envoi à domicile")
    fill_text_field_with('//*[@id="form_f27"]', "1")
    click_next_button()
    click_next_button()
    click_validate_button()


def click_connexion_toplink():
    demarches_en_ligne = driver.find_element(
        By.XPATH, '//*[@id="toplinks"]/span/a[1]')
    demarches_en_ligne.click()


def fill_and_submit_login_form_with_cred(ident, pw):
    username = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="id_username"]'))
    )
    password = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="id_password"]'))
    )
    username.clear()
    password.clear()
    username.send_keys(ident)
    password.send_keys(pw)
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="Mot_de_passe"]'))
    )
    driver.execute_script(
        "arguments[0].click();",
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="Mot_de_passe"]/div/form/input[2]')
            )
        ),
    )


def click_navbar_element(menu_page_id):
    navbar_element = driver.find_element(
        By.CSS_SELECTOR, f'[data-menu-page-id="{menu_page_id}"]'
    )
    navbar_element.click()
