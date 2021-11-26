"""
Logon with a user using login form and go to the list of forms
"""
from dotenv import load_dotenv
import os

from config import *
from functions import *

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

load_dotenv()

open_browser_at("https://staging.guichet-citoyen.be/")
click_connexion_toplink()
fill_and_submit_login_form_with_cred(os.environ.get(
    'seleniumUser'), os.environ.get('seleniumPassword'))
click_navbar_element(2)
