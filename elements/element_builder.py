from elements.element import Element


class ElementBuilder:

    def __init__(self, selector, locator, driver):
        self.selector = selector
        self.locator = locator
        self.driver = driver

    def element(self):
        return Element(self.selector, self.locator , self.driver)
