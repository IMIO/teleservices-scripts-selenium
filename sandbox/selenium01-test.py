"""
Open a chrome instance, click on a menu item and then on a form in the list
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument("headless")
# chrome_options.add_argument("--no-sandbox")  # needed for Linux
# chrome_options.add_argument("window-size=1900,1080")
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

ts_url = "https://staging.guichet-citoyen.be/"

# driver = webdriver.phantomjs(executable_path='/usr/local/bin/phantomjs')

driver.get(ts_url)

# cliquer sur demarches en ligne
demarches_en_ligne = driver.find_element(
    By.CSS_SELECTOR, "#nav > ul > li.menu-demarches-en-ligne > a"
)
demarches_en_ligne.click()

# certificat de nationalite
WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="columns"]/div[2]/div[2]/div/div[2]')
    )
)
driver.execute_script(
    "arguments[0].click();",
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="columns"]/div[2]/div[2]/div/div[2]/ul/li/a')
        )
    ),
)
driver.execute_script(
    "arguments[0].click();",
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="var_concerne_qui"]/div[2]/label[1]/span')
        )
    ),
)
