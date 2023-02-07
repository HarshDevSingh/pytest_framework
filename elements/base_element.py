import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException


class BaseElement:

    def __init__(self,selector,locator,driver):
        self.selector=selector
        self.locator=locator
        self.driver=driver

    def is_element_clickable(self) -> bool:
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((self.selector,self.locator, )))
            return element
        except ElementNotInteractableException as e:
            print(e)
            return False

    def _find_element(self):
        return self.driver.find_element(self.selector,self.locator)

    def is_element_visible(self):
        element = self._find_element()
        if element.is_displayed():
            return True
        else:
            return False

    def send_keys(self, keys):
        element = self._find_element()
        if element:
            element.send_keys(keys)
        else:
            raise Exception(f"Failed to send keys to element {self.selector}")

    def click(self):
        element = self._find_element()
        if element:
            element.click()
        else:
            raise Exception(f"Failed to click {self.selector}")