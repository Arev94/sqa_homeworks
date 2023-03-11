import time
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By



@pytest.mark.usefixtures("get_driver")
class Test:
    def test_login(self):
        username_text = "Admin"
        password = "admin123"

        username_input = self.get_wait.wait_for_element(By.CSS_SELECTOR, "input[name='username']")
        username_input.send_keys(username_text)

        self.driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        self.get_wait.wait_for_element(By.XPATH, '//*[text() ="My Info"]').click()

        firstname = self.get_wait.wait_for_element(By.CSS_SELECTOR, 'input[name="firstName"]')
        firstname.send_keys(Keys.CONTROL + 'a')
        firstname.send_keys(Keys.BACK_SPACE)
        firstname.send_keys("Clark")

        middlename = self.driver.find_element(By.CSS_SELECTOR, 'input[name="middleName"]')
        middlename.click()
        middlename.send_keys(Keys.CONTROL + 'a')
        middlename.send_keys(Keys.BACK_SPACE)
        middlename.send_keys("Little")

        lastname = self.driver.find_element(By.CSS_SELECTOR, 'input[name="lastName"]')
        lastname.click()
        lastname.send_keys(Keys.CONTROL + 'a')
        lastname.send_keys(Keys.BACK_SPACE)
        lastname.send_keys('Jonathan')

        input_list = self.get_wait.wait_for_list_size_change(By.CSS_SELECTOR, '.oxd-input', 13)

        nick_name = input_list[4]
        nick_name.click()
        nick_name.send_keys(Keys.CONTROL + 'a')
        nick_name.send_keys(Keys.BACK_SPACE)

        emp_id = input_list[5]
        emp_id.click()
        emp_id.send_keys(Keys.CONTROL + 'a')
        emp_id.send_keys(Keys.BACK_SPACE)
        emp_id.send_keys('0023')

        other_name = input_list[6]
        other_name.click()
        other_name.send_keys(Keys.CONTROL + 'a')
        other_name.send_keys(Keys.BACK_SPACE)

        dr_lic_num = input_list[7]
        dr_lic_num.click()
        dr_lic_num.send_keys(Keys.CONTROL + 'a')
        dr_lic_num.send_keys(Keys.BACK_SPACE)
        dr_lic_num.send_keys('12AM022')

        #lic_expiry_date
        input_list[8].click()
        self.get_wait.wait_for_element(By.CSS_SELECTOR, '.oxd-calendar-selector-month-selected').click()
        time.sleep(5)
        self.get_wait.wait_for_element(By.XPATH, '//li[text() = "May"]').click()
        time.sleep(5)
        self.get_wait.wait_for_element(By.CSS_SELECTOR, '.oxd-calendar-selector-year').click()
        self.get_wait.wait_for_element(By.XPATH, '//li[text() = "2023"]').click()
        self.get_wait.wait_for_element(By.XPATH, '//div[text() = "21"]').click()

        ssn_num = input_list[9]
        ssn_num.click()
        ssn_num.send_keys(Keys.CONTROL + 'a')
        ssn_num.send_keys(Keys.BACK_SPACE)
        ssn_num.send_keys('3434334')

        sin_num = input_list[10]
        sin_num.click()
        sin_num.send_keys(Keys.CONTROL + 'a')
        sin_num.send_keys(Keys.BACK_SPACE)
        sin_num.send_keys('123 123 123')

        birth_date = input_list[11]
        birth_date.click()
        self.get_wait.wait_for_element(By.CSS_SELECTOR, '.oxd-calendar-selector-month').click()
        self.get_wait.wait_for_element(By.XPATH, '//li[text() = "June"]').click()
        self.get_wait.wait_for_element(By.CSS_SELECTOR, '.oxd-calendar-selector-year').click()
        self.get_wait.wait_for_element(By.XPATH, '//li[text() = "1987"]').click()
        self.get_wait.wait_for_element(By.XPATH, '//div[text() = "12"]').click()


        military_service = input_list[12]
        military_service.click()
        military_service.send_keys(Keys.CONTROL + 'a')
        military_service.send_keys(Keys.BACK_SPACE)
        military_service.send_keys('DD214')

        selects_input_list = self.get_wait.wait_for_list_size_change(By.CSS_SELECTOR, '.oxd-select-text', 3)
        selects_input_text_list = self.get_wait.wait_for_list_size_change(By.CSS_SELECTOR, 'div[class ="oxd-select-text-input"]', 3)

        selects_input_list[0].click()
        select_country = self.get_wait.wait_for_element(By.XPATH, '//span[text() ="Andorran"]')
        if select_country.text == selects_input_text_list[0].text:
            pass
        else:
            select_country.click()

        selects_input_list[1].click()
        select_marital_status = self.get_wait.wait_for_element(By.XPATH, '//span[text()="Married"]')
        if select_marital_status.text == selects_input_text_list[1].text:
            pass
        else:
            select_marital_status.click()

        try:
            gender = self.get_wait.wait_for_element(By.XPATH, '(//span[@class="oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input"])[1]')
            gender.click()
        except:
            pass

        self.get_wait.wait_for_element(By.CSS_SELECTOR, "button[type = 'submit']").click()
        assert firstname.get_attribute('value') == "Clark"
















