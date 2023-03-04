import time
import pytest

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



@pytest.mark.usefixtures("get_driver")
class TestActions:

    def test_checkbox_buttons(self):
        bmw_checkbox = self.get_wait.wait_for_element(By.CSS_SELECTOR, 'input[id="bmwcheck"]')
        benz_checkbox = self.driver.find_element(By.CSS_SELECTOR, "input[id = 'benzcheck']")
        honda_checkbox = self.driver.find_element(By.CSS_SELECTOR, "input[id = 'hondacheck']")


        assert not bmw_checkbox.is_selected()
        assert not honda_checkbox.is_selected()
        assert not benz_checkbox.is_selected()

        bmw_checkbox.click()
        assert bmw_checkbox.is_selected()
        assert not honda_checkbox.is_selected()
        assert not benz_checkbox.is_selected()

        benz_checkbox.click()
        assert benz_checkbox.is_selected()
        assert not honda_checkbox.is_selected()
        assert bmw_checkbox.is_selected()

        honda_checkbox.click()
        assert benz_checkbox.is_selected()
        assert honda_checkbox.is_selected()
        assert bmw_checkbox.is_selected()

        benz_checkbox.click()
        assert not benz_checkbox.is_selected()
        assert honda_checkbox.is_selected()
        assert bmw_checkbox.is_selected()



    def test_radio_buttons(self):

        bmw_radio = self.get_wait.wait_for_element(By.CSS_SELECTOR, "input[id='bmwradio']")
        benz_radio = self.driver.find_element(By.CSS_SELECTOR, "input[id = 'benzradio']")
        honda_radio = self.driver.find_element(By.CSS_SELECTOR, "input[id = 'hondaradio']")

        assert not bmw_radio.is_selected()
        assert not benz_radio.is_selected()
        assert not honda_radio.is_selected()

        bmw_radio.click()
        assert bmw_radio.is_selected()
        assert not benz_radio.is_selected()
        assert not honda_radio.is_selected()

        benz_radio.click()
        assert not bmw_radio.is_selected()
        assert benz_radio.is_selected()
        assert not honda_radio.is_selected()

        honda_radio.click()
        assert not bmw_radio.is_selected()
        assert not benz_radio.is_selected()
        assert honda_radio.is_selected()

    def test_dropdown(self):

        cars = self.get_wait.wait_for_element(By.CSS_SELECTOR, 'select[id="carselect"]')
        cars_select = Select(cars)

        cars_select.select_by_index(0)
        assert cars_select.first_selected_option.text == "BMW"

        cars_select.select_by_index(1)
        assert cars_select.first_selected_option.text == "Benz"

        cars_select.select_by_index(2)
        assert cars_select.first_selected_option.text == "Honda"

    def test_multi_select_dropdawn(self):

        fruits = self.get_wait.wait_for_element(By.CSS_SELECTOR, 'select[id="multiple-select-example"]')
        fruits_select = Select(fruits)

        fruits_select.select_by_index(0)
        fruits_select.select_by_visible_text("Orange")
        fruits_select.select_by_value("peach")

        fruits_select.deselect_by_index(0)
        fruits_select.deselect_by_visible_text("Orange")
        fruits_select.deselect_by_value("peach")

        fruits_select.select_by_visible_text("Orange")
        fruits_select.select_by_value("peach")
        fruits_select.deselect_all()

    def test_autosuggest_input(self):

        input_suggest = self.get_wait.wait_for_element(By.CSS_SELECTOR, 'input[id="autosuggest"]')
        input_suggest.click()
        input_suggest.send_keys("I hope i write right")


    def test_disabled(self):

        input_text = "Hi guys"

        disabled_input = self.get_wait.wait_for_element(By.CSS_SELECTOR, 'input[id="enabled-example-input"]')
        assert disabled_input.is_enabled()
        disabled_input.send_keys(input_text)
        time.sleep(5)

        disabled_button = self.driver.find_element(By.CSS_SELECTOR, 'input[id="disabled-button"]')
        disabled_button.click()

        assert not disabled_input.is_enabled()

        enabled_button = self.driver.find_element(By.CSS_SELECTOR, 'input[id="enabled-button"]')
        enabled_button.click()

        assert disabled_input.is_enabled()
        assert disabled_input.get_attribute('value') == input_text


    def test_hidden_element(self):


        hidden_text = "Hidden text"
        hidden_input = self.get_wait.wait_for_element(By.CSS_SELECTOR, 'input[id="displayed-text"]')
        hide_button = self.driver.find_element(By.CSS_SELECTOR, 'input[id="hide-textbox"]')
        show_button = self.driver.find_element(By.CSS_SELECTOR, 'input[id="show-textbox"]')

        assert hidden_input.is_displayed()

        hidden_input.send_keys(hidden_text)
        hide_button.click()

        assert not hidden_input.is_displayed()
        time.sleep(5)

        show_button.click()

        assert hidden_input.get_attribute('value') == hidden_text
        time.sleep(5)

    def test_mouse_hover(self):

        drop_button = self.get_wait.wait_for_element(By.CSS_SELECTOR, 'button[id="mousehover"]')
        achains = ActionChains(self.driver)

        achains.move_to_element(drop_button).perform()
        self.get_wait.wait_for_element(By.XPATH,'//a[text()="Top"]').click()

        achains.move_to_element(drop_button).perform()
        self.get_wait.wait_for_element(By.XPATH, '//a[text()="Reload"]').click()

    def test_alert(self):

        alert_input = self.get_wait.wait_for_element(By.CSS_SELECTOR,'input[name = "enter-name"]')
        user_1 = "Aram"
        user_2 = "Ani"

        alert_input.send_keys(user_1)
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, 'input[id="alertbtn"]').click()
        alert = self.driver.switch_to.alert

        assert alert.text == f'Hello {user_1}, share this practice page and share your knowledge'
        alert.accept()

        alert_input.send_keys(user_2)
        self.driver.find_element(By.CSS_SELECTOR, 'input[id="confirmbtn"]').click()

        confirm = self.driver.switch_to.alert

        assert confirm.text == f'Hello {user_2}, Are you sure you want to confirm?'
        confirm.accept()

        alert_input.send_keys(user_2)
        self.driver.find_element(By.CSS_SELECTOR, 'input[id="confirmbtn"]').click()
        confirm.dismiss()


    def test_switch_tab(self):

        main_handle = self.driver.current_window_handle
        self.get_wait.wait_for_element(By.CSS_SELECTOR, 'a[id="opentab"]').click()

        all_handles = self.driver.window_handles

        for handle in all_handles:
            if handle != main_handle:
                self.driver.switch_to.window(handle)
                self.get_wait.wait_for_element(By.XPATH, "//h4[contains(text(),'beginners')]").click()

                self.driver.close()
                break

        self.driver.switch_to.window(main_handle)
        self.get_wait.wait_for_element(By.CSS_SELECTOR,'a[id="opentab"]').click()




test1 = TestActions()

test1.test_dropdown()
test1.test_multi_select_dropdawn()
test1.test_checkbox_buttons()
test1.test_autosuggest_input()
test1.test_disabled()
test1.test_hidden_element()
test1.test_alert()
test1.test_switch_tab()


