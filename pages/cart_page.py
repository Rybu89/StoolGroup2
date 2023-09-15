from base.base_class import Base


class Cart_page(Base):

    def __init__(self):
        super().__init__()


    # Locators

    locator_checkout_button = ['xpath', '//a[contains(text(), "Оформить заказ")]']

    # Actions

    def click_checkout_button(self):
        self.click_element(self.locator_checkout_button)
        self.save_cookies('order_products')
        print("___Click Button 'Оформить заказ'")
