import time

from base.base_class import Base
from pages.cart_page import Cart_page
from pages.checkout_page import Checkout_page
from pages.main_page import Main_page
from pages.tables_page import Tables_page

base = Base()
MP = Main_page()
TP = Tables_page()
CP = Cart_page()
ChP = Checkout_page()


def test_id_01(from_module, from_test_id_01):

        """    Проверка, быстрого фильтра на странице "Столы". """

        base.open_page(MP.url)
        MP.click_tables_button()

        TP.select_price_tables_scroll(TP.step_scroll_filter_price_rang_min, TP.step_scroll_filter_price_rang_max)
        TP.select_quick_filters_in_stock()
        TP.select_quick_filters_category_tables()
        TP.select_quick_filters_brand_stool_group()
        TP.select_quick_filters_color_walnut()

        # base.browser.find_element(*base.locator_ads_500_bonus).click()
        #
        # base.click_element(TP.locator_quick_filters_price_range)
        #
        # base.catch_ads()


def test_id_02(from_test_id_02):

        """ Добавление товара в корзину. """

        TP.select_first_product_buy_button()
        TP.select_first_product_one_click_button()

def test_id_03(from_test_id_03):

        """ Оформление заказа. """

        ChP.add_contact_information()
        ChP.click_checkbox_self_delivery()
        ChP.click_checkbox_private_person()
        ChP.click_radio_button_online_payment()
        ChP.click_radio_button_promocode()
        ChP.input_promocode()
        ChP.click_apply_button()

