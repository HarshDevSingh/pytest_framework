from elements.base_element import BaseElement


class Element(BaseElement):
    def __init__(self,selector,locator,driver):
        super().__init__(selector,locator,driver)