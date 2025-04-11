import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pom.login_page import LoginPage
from utils.excel_util import read_test_data, write_test_result

@pytest.mark.parametrize("test_id,username,password,date,time,tester,result", read_test_data("test_data.xlsx"))
def test_login(test_id, username, password, date, time, tester, result):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login_page = LoginPage(driver)
    login_page.login(username, password)

    if login_page.is_login_successful():
        write_test_result("test_data.xlsx", test_id, "Passed")
        assert True
    else:
        write_test_result("test_data.xlsx", test_id, "Failed")
        assert False

    driver.quit()
