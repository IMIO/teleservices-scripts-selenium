# Generated by Selenium IDE
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def click(xpath):
    print("Clicking on element (xpath) : ", xpath)
    driver.execute_script(
        "arguments[0].click();",
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, xpath))),
    )


class TestCheretvilainavocat():

    def setup_method(self, method):
        chrome_options = Options()
        # chrome_options.add_argument("--no-sandbox")  # needed for Linux
        # chrome_options.add_argument("--headless")  # needed for Linux
        chrome_options.add_argument("window-size=1900,1080")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.vars = {}
        self.wait = WebDriverWait(self.driver, 10)

    def teardown_method(self, method):
        self.driver.quit()

    def next_page(self):
        self.driver.execute_script(
            "arguments[0].click();",
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "submit"))),
        )

    def test_cheretvilainavocat(self):
        self.driver.get(
            "https://staging2-formulaires.guichet-citoyen.be/bac-a-sable/cher-et-vilain/")
        self.driver.maximize_window()
        dropdown = self.driver.find_element(By.ID, "form_f47")
        dropdown.find_element(By.XPATH, "//option[. = 'Avocat']").click()
        element = self.driver.find_element(By.ID, "form_f47")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.ID, "form_f47")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.ID, "form_f47")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        element = self.driver.find_element(By.ID, "form_f49")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.ID, "form_f49")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.ID, "form_f49")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.ID, "form_f50").click()
        self.driver.find_element(By.ID, "columns").click()
        element = self.driver.find_element(By.ID, "columns")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.next_page()
        self.next_page()
        self.next_page()
        self.driver.execute_script(
            "arguments[0].click();",
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Acc??der au panier"))),
        )
        # self.driver.find_element(By.ID, "pay").click() # n??cessite une connexion


current_test = TestCheretvilainavocat()
current_test.setup_method("")
current_test.test_cheretvilainavocat()
current_test.teardown_method("")
