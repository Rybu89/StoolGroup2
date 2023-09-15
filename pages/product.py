from base.base_class import Base


class Product_page(Base):

    def __init__(self):
        super().__init__()

    # Locators

    locator_buy_product = ['xpath', '// button[ @ id = "button_cart_75907"']
