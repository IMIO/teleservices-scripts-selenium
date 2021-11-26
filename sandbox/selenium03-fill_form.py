from dotenv import load_dotenv
import os

from functions import *

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

load_dotenv()

open_browser_at("https://staging2.guichet-citoyen.be/")
click_connexion_toplink()
fill_and_submit_login_form_with_cred(os.environ.get(
    'seleniumUser'), os.environ.get('seleniumPassword'))
click_navbar_element(2)
fill_cert_nationalite_form(
    "Python",
    "Selenium",
    "00000000097",
    "18/06/1989",
    "Rue Léon Morel",
    "1",
    "5000",
    "Isnes",
    "daniel.muyshond+selenium@imio.be",
    "0471541363",
)
