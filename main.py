from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import os

# Initial set of the web browser
driver: webdriver.Chrome = webdriver.Chrome()
driver.get("https://www.linkedin.com")

user_password: str = os.environ.get("LINKEDIN_PASSWORD")
user_name: str = os.environ.get("USERNAME")


def log_in(user=user_name, password=user_password) -> None:
    """
    Automates login to LinkedIn using Selenium.

    Parameters:
    - user (str): Username or email for login.
    - password (str): User's account password.

    Assumes Selenium WebDriver is initialized and on LinkedIn's login page.
    """
    try:
        username_input: WebElement = driver.find_element_by_id(id_="session_key")
        username_input.send_keys(user)
        password_input: WebElement = driver.find_element_by_id(id_="session_password")
        password_input.send_keys(password)
        login_button: WebElement = driver.find_elements_by_xpath(
            xpath='//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')
        login_button[0].click()
    except NoSuchElementException as e:
        print(f"Element not found: {e}")
    except WebDriverException as e:
        print(f"WebDriver encountered an issue: {e}")

log_in()
