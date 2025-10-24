from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.saucedemo.com/"
USUARIO = "standard_user"
PASSWORD = "secret_sauce"


def iniciar_driver():
    """Inicializa el navegador y devuelve el driver con esperas configuradas."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)
    return driver, wait


def login(driver, wait):
    """Realiza el login en SauceDemo."""
    driver.get(URL)
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    wait.until(EC.url_contains("/inventory.html"))
