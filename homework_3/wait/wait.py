from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as condition

from test_for_orange.wait.get_by import get_by_type


class Wait:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator_type, locator,
                         timeout=30):
        element = None
        try:
            by_type = get_by_type(locator_type)
            print("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be visible")
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(condition.visibility_of_element_located((by_type, locator)))
            print("Element appeared on the web page")
        except NoSuchElementException:
            print("Element not appeared on the web page")
        return element

    def wait_for_element_to_be_clickable(self, locator_type, locator,
                                         timeout=30):
        element = None
        try:
            by_type = get_by_type(locator_type)
            print("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be visible")
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(condition.element_to_be_clickable((by_type, locator)))
            print("Element appeared on the web page")
        except NoSuchElementException:
            print("Element not appeared on the web page")
        return element

    def wait_for_element_to_be_selected(self, element,
                                        timeout=30):
        selected_element = None
        try:
            print("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be visible")
            wait = WebDriverWait(self.driver, timeout)
            selected_element = wait.until(condition.element_selection_state_to_be(element, True))
            print("Element appeared on the web page")
        except NoSuchElementException:
            print("Element not appeared on the web page")
        return selected_element

    def wait_for_list_size_change(self, locator_type, locator, size, timeout=30):
        """
        Wait for the size of a list of elements to change to a specific value.
        Args
            locator: a tuple (By.<method>, <selector>) that identifies the list of elements
            size: an integer representing the expected size of the list of elements
        Raises:
            TimeoutException if the size of the list of elements does not change to the expected value
        """

        try:
            by_type = get_by_type(locator_type)
            wait = WebDriverWait(self.driver, timeout)
            wait.until(lambda driver: len(driver.find_elements(by_type, locator)) == size)
            return self.driver.find_elements(by_type, locator)
        except TimeoutException:
            print(f"Timed out waiting for {size} elements to be present")
            return False
