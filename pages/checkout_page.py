from base.base_class import Base

class Checkout_page(Base):

    def __init__(self):
        super().__init__()

    # Test data

    first_name = 'Иван'
    last_name = 'Иванов'
    email = 'xxx@mail.ru'
    phone = '9001234567'
    promocode = '12345'

    # Locators

    locator_first_name = ['xpath', '//input[@id="firstname"]']
    locator_last_name = ['xpath', '//input[@id="lastname"]']
    locator_email = ['xpath', '//input[@id="email"]']
    locator_phone = ['xpath', '//input[@id="phone"]']
    locator_self_delivery_radio_button = ['xpath', '//input[@id="sh_0_11"]']
    locator_legal_person_radio_button = ['xpath', '//div[@id="title_tab3"]']
    locator_private_person_radio_button = ['xpath', '//div[@id="title_tab1"]']
    locator_online_payment_radio_button = ['xpath', '//input[@id="radio_28"]']
    locator_promocode_radio_button = ['xpath', '//div[@id="promocode-tab"]']
    locator_promocode_field = ['xpath', '//input[@id="coupon_field"]']
    locator_apply_button = ['xpath', '//button[@type="button" and contains(text(), "Применить")]'] #['xpath', '//button[@class="promocode__button js-promo-btn" and contains(text(), "Применить")]']
    locator_bonus_radio_button = ['xpath', '//div[@id="bonuses-tab"]']


    # Actions

    def input_first_name(self):
        self.get_clikable_element(self.locator_first_name).clear()
        self.get_clikable_element(self.locator_first_name).send_keys(self.first_name)
        print("___Input first name: " + self.first_name)

    def input_last_name(self):
        self.get_clikable_element(self.locator_last_name).clear()
        self.get_clikable_element(self.locator_last_name).send_keys(self.last_name)
        print("___Input last name: " + self.last_name)

    def input_email(self):
        self.get_clikable_element(self.locator_email).clear()
        self.get_clikable_element(self.locator_email).send_keys(self.email)
        print("___Input email: " + self.email)

    def input_phone(self):
        self.get_clikable_element(self.locator_phone).clear()
        self.get_clikable_element(self.locator_phone).send_keys(self.phone)
        print("___Input phone: " + self.phone)

    def input_promocode(self):
        self.scroll_browser(0, 600)
        self.get_clikable_element(self.locator_promocode_field).clear()
        self.get_clikable_element(self.locator_promocode_field).send_keys(self.promocode)
        print("___Input promocode: " + self.promocode)

    def click_checkbox_self_delivery(self):
        self.scroll_browser(0, 600)
        value = self.check_and_click_checkbox(self.locator_self_delivery_radio_button, 'checked', 'true')
        print("___Click Checkbox 'Самовывоз  по адресу  — 15 км от МКАД по М10'. Status before click: " + value[0] + "." + " Status after click: " + value[
            1] + "." + " Check PASSED")

    def click_checkbox_private_person(self):
        value = self.check_and_click_checkbox(self.locator_private_person_radio_button, 'aria-selected', 'true')
        print("___Click Checkbox 'Физическое лицо'. Status before click: " + value[0] + "." + " Status after click: " + value[
            1] + "." + " Check PASSED")

    def click_radio_button_legal_person(self):

        value = self.check_and_click_checkbox(self.locator_legal_person_radio_button, 'aria-selected', 'true')
        print("___Click Checkbox 'Юридическое лицо'. Status before click: " + value[0] + "." + " Status after click: " + value[
            1] + "." + " Check PASSED")

    def click_radio_button_online_payment(self):

        """ Выбор способа оплаты - онлайн """

        value = self.check_and_click_checkbox(self.locator_online_payment_radio_button, 'checked', 'true')      # Проверка и нажатие на кнопку
        print("___Click Checkbox 'Онлайн оплата'. Status before click: " + value[0] + "." + " Status after click: " + value[
            1] + "." + " Check PASSED")

    def click_radio_button_promocode(self):

        """ Использование промокода """

        try :
            value = self.check_and_click_checkbox(self.locator_promocode_radio_button, 'aria-selected', 'true') # Проверка и нажатие на кнопку
        except :
            # На случай если промокод выбран, но по умолчанию имеет значение aria-selected = false """
            self.click_element(self.locator_bonus_radio_button)     # Переключение на соседнюю кнопку
            value = self.check_and_click_checkbox(self.locator_promocode_radio_button, 'aria-selected', 'true')     # Повторная проверка и нажатие

        print("___Click Checkbox 'Промокод'. Status before click: " + value[0] + "." + " Status after click: " + value[
            1] + "." + " Check PASSED")

    def click_apply_button(self):
        self.click_element(self.locator_apply_button)
        print("___Click Button 'Применить'")

    def add_contact_information(self):

        """ Заполнение раздела 'Контактная информация """

        # self.load_cookies('order_products_1')
        self.input_first_name()     # Ввод в поле Имя
        self.input_last_name()      # Ввод в поле Фамилия
        self.input_phone()      # Ввод в поле Телефон
        self.input_email()      # Ввод в поле Электронная почта
        self.screenshot('add_contact_information')      # Снимок экрана

    def select_self_delivery_method(self):

        """ Выбор способа доставки - самомвывоз """

        self.click_checkbox_self_delivery()     # Проверка и нажатие на чек-бокс Самовывоз

    def select_legal_person_entity(self):

        """ Выбор физического лица """

        self.click_radio_button_legal_person()      # Проверка и нажатие на чек-бокс Физическое лицо
