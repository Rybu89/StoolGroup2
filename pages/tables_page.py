import time

from selenium.webdriver import ActionChains

import base
from base.base_class import Base


class Tables_page(Base):

    def __init__(self):
        super().__init__()
        self.ActionChains = ActionChains(self.browser)


    # Test data

    url = 'https://stoolgroup.ru/stoly/'
    step_scroll_filter_price_rang_min = [25, 0]
    step_scroll_filter_price_rang_max = [-50, 0]


    # Locators

    locator_page_title = ["xpath", '//h1[@class="tp_h-2 mb-0"]']
    value_locator_page_title = 'Столы'
        # quick filters
    locator_quick_filters_price_range = ["xpath", '//div[@class="spoiler__title" and contains(text(), "Диапазон цены")]']
    locator_quick_filters_price_range_min_scroll = ["xpath", '//*[@id="slider_116_102"]/span[1]']
    locator_quick_filters_price_range_max_scroll = ["xpath", '//*[@id="slider_116_102"]/span[2]']
    locator_quick_filters_price_range_min_input = ["xpath", '//input[@id="slider_116_102_left"]']
    locator_quick_filters_price_range_max_input = ["xpath", '//input[@id="slider_116_102_right"]']

    locator_quick_filters_in_stock_button = ["xpath", '//div[@class="spoiler__title" and contains(text(), "В наличии")]']
    locator_quick_filters_in_stock_visible_checkbox = ["xpath", '//ul[@id="ranges_116_135"]/li/label/div[1]']
    locator_quick_filters_in_stock_checkbox = ["xpath", '//*[@id="elm_checkbox_116_135_Y"]']

    locator_quick_filters_category_button = ["xpath", '//div[@class="spoiler__title" and contains(text(), "Категория")]']
    locator_quick_filters_category_visible_checkbox = ["xpath", '(//div[@class="filters-checkbox__info" and contains(text(), "Столы")])[3]']
    locator_quick_filters_category_checkbox_tables = ["xpath", '//input[@id="elm_checkbox_116_72_7048"]']

    locator_quick_filters_brand_button = ["xpath", '//div[@class="spoiler__title" and contains(text(), "Бренд")]']
    locator_quick_filters_brand_visible_checkbox = ["xpath", '(//div[@class="filters-checkbox__info" and contains(text(), "Stool Group")])[2]']
    locator_quick_filters_brand_checkbox_stool_group = ["xpath", '//input[@id="elm_checkbox_116_21_275"]']

    locator_quick_filters_color_button = ["xpath", '//div[@class="spoiler__title" and contains(text(), "Цвет")]']
    locator_quick_filters_color_visible_checkbox = ["xpath", '(//div[@class="filters-checkbox__info" and contains(text(), "орех")])[2]']
    locator_quick_filters_color_checkbox_walnut = ["xpath", '//input[@id="elm_checkbox_116_81_14283"]']

    # products

    locator_first_product_buy_button = ["xpath", '/html/body/div[9]/div/div[1]/div[1]/form/div[2]/div/div[1]/a[1]']
    locator_first_product_name = ["xpath", '//div[@id="row_pagination"]/div[1]/form/a/div[3]/div[2]']
    locator_first_product_name_in_cart = ["xpath", '//form[@id="checkout_form"]/div[2]/div/div[1]/div/a']
    locator_cart = ["xpath", '//div[@id="cart_amount"]']
    locator_first_product_buy_one_click_button = ["xpath", '//div[@id="row_pagination"]/div[1]/form/div[2]/div/div[1]/a[2]']
    locator_first_product_name_in_order = ["xpath", '//div[@id="call_request_modal"]/form/div[1]/div[1]/div[2]/div']


    # Getters

    def get_value_quick_filters_price_range_min(self):
        return self.get_value_text(self.locator_quick_filters_price_range_min_input)

    def get_value_quick_filters_price_range_max(self):
        return self.get_value_text(self.locator_quick_filters_price_range_max_input)

    def get_name_first_product(self):
        return self.get_text(self.locator_first_product_name)

    def get_name_first_product_in_cart(self):
        return self.get_text(self.locator_first_product_name_in_cart)

    def get_name_first_product_in_order(self):
        return self.get_text(self.locator_first_product_name_in_order)


    # Actions

    def click_quick_filters_price_range_button(self):
        self.click_element(self.locator_quick_filters_price_range)
        print("___Click Button 'Диапазон цены'")


    def click_quick_filters_in_stock_button(self):
        value = self.check_and_click_dropdown_is_displayed(self.locator_quick_filters_in_stock_button, self.locator_quick_filters_in_stock_visible_checkbox)
        print("___Click Dropdown 'В наличии'. Status before click: " + str(value[0]) + "." + " Status after click: " + str(value[1]) + "." + " Check PASSED")

    def click_quick_filters_in_stock_checkbox(self):
        value = self.check_and_click_checkbox(self.locator_quick_filters_in_stock_checkbox, 'checked', 'true')
        print("___Click Checkbox 'В наличии'. Status before click: " + value[0] + "." + " Status after click: " + value[1] + "." + " Check PASSED")

    def click_quick_filters_category_button(self):
        value = self.check_and_click_dropdown_is_displayed(self.locator_quick_filters_category_button, self.locator_quick_filters_category_visible_checkbox)
        print("___Click Dropdown 'Категория'. Status before click: " + str(value[0]) + "." + " Status after click: " + str(value[1]) + "." + " Check PASSED")

    def click_quick_filters_category_checkbox_tables(self):
        value = self.check_and_click_checkbox(self.locator_quick_filters_category_checkbox_tables, 'checked', 'true')
        print("___Click Checkbox 'Столы'. Status before click: " + value[0] + "." + " Status after click: " + value[1] + "." + " Check PASSED")

    def click_quick_filters_brand_button(self):
        value = self.check_and_click_dropdown_is_displayed(self.locator_quick_filters_brand_button, self.locator_quick_filters_brand_visible_checkbox)
        print("___Click Dropdown 'Бренд'. Status before click: " + str(value[0]) + "." + " Status after click: " + str(value[1]) + "." + " Check PASSED")

    def click_quick_filters_brand_checkbox_stool_group(self):
        value = self.check_and_click_checkbox(self.locator_quick_filters_brand_checkbox_stool_group, 'checked', 'true')
        print("___Click Checkbox 'Stool Group'. Status before click: " + value[0] + "." + " Status after click: " + value[1] + "." + " Check PASSED")

    def click_quick_filters_color_button(self):
        value = self.check_and_click_dropdown_is_displayed(self.locator_quick_filters_color_button, self.locator_quick_filters_color_visible_checkbox)
        print("___Click Dropdown 'Цвет'. Status before click: " + str(value[0]) + "." + " Status after click: " + str(
            value[1]) + "." + " Check PASSED")

    def click_quick_filters_color_checkbox_walnut(self):
        value = self.check_and_click_checkbox(self.locator_quick_filters_color_checkbox_walnut, 'checked', 'true')
        print("___Click Checkbox 'Орех'. Status before click: " + value[0] + "." + " Status after click: " + value[
            1] + "." + " Check PASSED")

    def click_first_product_buy_button(self):
        self.click_element(self.locator_first_product_buy_button)
        print("___Click Button 'Купить'")

    def click_first_product_buy_one_click_button(self):
        self.click_element(self.locator_first_product_buy_one_click_button)
        print("___Click Button 'Купить в один клик'")

    def click_cart(self):
        self.click_element(self.locator_cart)
        print("___Click Button 'Cart'")


    # Methods

    def select_price_tables_scroll(self, step_min_price, step_max_price):
        self.click_quick_filters_price_range_button()
        min_price_before = self.get_value_quick_filters_price_range_min()
        self.scroll_and_release(self.locator_quick_filters_price_range_min_scroll, self.step_scroll_filter_price_rang_min)
        min_price_after = self.get_value_quick_filters_price_range_min()

        assert int(min_price_before) < int(min_price_after)
        print("___Select min price " + str(min_price_after) + " Min price before = " + str(min_price_before)+ " Check PASSED")

        time.sleep(5)

        self.click_quick_filters_price_range_button()
        max_price_before = self.get_value_quick_filters_price_range_max()
        self.scroll_and_release(self.locator_quick_filters_price_range_max_scroll, self.step_scroll_filter_price_rang_max)
        max_price_after = self.get_value_quick_filters_price_range_max()

        assert int(max_price_before) > int(max_price_after)
        print("___Select max price " + str(min_price_after) + " Max price before = " + str(max_price_before) + " Check PASSED")

    def select_quick_filters_in_stock(self):
        self.click_quick_filters_in_stock_button()
        self.click_quick_filters_in_stock_checkbox()

    def select_quick_filters_category_tables(self):
        self.click_quick_filters_category_button()
        self.click_quick_filters_category_checkbox_tables()

    def select_quick_filters_brand_stool_group(self):
        self.click_quick_filters_brand_button()
        self.click_quick_filters_brand_checkbox_stool_group()

    def select_quick_filters_color_walnut(self):
        self.click_quick_filters_color_button()
        self.click_quick_filters_color_checkbox_walnut()

    def select_first_product_buy_button(self):
        name_befor = self.get_name_first_product()
        self.move_to_element(self.locator_first_product_name)
        self.click_first_product_buy_button()
        self.move_to_element(self.locator_cart)
        time.sleep(5)
        self.click_cart()
        name_after = self.get_name_first_product_in_cart()
        assert name_befor == name_after
        print("___Select product " + name_after + " PASSED")
        self.save_cookies('order_products_1')


    def select_first_product_one_click_button(self):
        self.load_cookies('select_products')
        name_befor = self.get_name_first_product()
        self.move_to_element(self.locator_first_product_name)
        self.click_first_product_buy_one_click_button()
        name_after = self.get_name_first_product_in_order()
        assert name_befor == name_after
        print("___Select product " + name_after + " PASSED")