from base.base_class import Base


class Checkout_page(Base):

    def __init__(self):
        super().__init__()

    # Test data

    first_name = 'Иван'
    last_name = 'Иванов'
    email = 'xxx@mail.ru'
    phone = '9001234567'
    promo_code = '12345'

    # Locators

    locator_first_name = ['xpath', '//input[@id="firstname"]']
    locator_last_name = ['xpath', '//input[@id="lastname"]']
    locator_email = ['xpath', '//input[@id="email"]']
    locator_phone = ['xpath', '//input[@id="phone"]']
    locator_self_delivery_radio_button = ['xpath', '//input[@id="sh_0_11"]']
    locator_legal_person_radio_button = ['xpath', '//div[@id="title_tab3"]']
    locator_private_person_radio_button = ['xpath', '//div[@id="title_tab1"]']
    locator_online_payment_radio_button = ['xpath', '//input[@id="radio_28"]']
    locator_promo_code_radio_button = ['xpath', '//div[@id="promocode-tab"]']
    locator_promo_code_field = ['xpath', '//input[@id="coupon_field"]']
    locator_apply_button = ['xpath', '//button[@type="button" and contains(text(), "Применить")]']
    locator_bonus_radio_button = ['xpath', '//div[@id="bonuses-tab"]']

    # Actions

    def input_first_name(self):

        """  Ввод в поле - Имя. """

        self.get_clickable_element(self.locator_first_name).clear()
        self.get_clickable_element(self.locator_first_name).send_keys(self.first_name)
        print("___Input first name: " + self.first_name)

    def input_last_name(self):

        """  Ввод в поле - Фамилия. """

        self.get_clickable_element(self.locator_last_name).clear()
        self.get_clickable_element(self.locator_last_name).send_keys(self.last_name)
        print("___Input last name: " + self.last_name)

    def input_email(self):

        """  Ввод в поле - Email. """

        self.get_clickable_element(self.locator_email).clear()
        self.get_clickable_element(self.locator_email).send_keys(self.email)
        print("___Input email: " + self.email)

    def input_phone(self):

        """  Ввод в поле - Телефон. """

        self.get_clickable_element(self.locator_phone).clear()
        self.get_clickable_element(self.locator_phone).send_keys(self.phone)
        print("___Input phone: " + self.phone)

    def input_promo_code(self):

        """  Ввод в поле - Промокод. """

        self.scroll_browser(0, 600)
        self.get_clickable_element(self.locator_promo_code_field).clear()
        self.get_clickable_element(self.locator_promo_code_field).send_keys(self.promo_code)
        print("___Input promo-code: " + self.promo_code)

    def click_radio_button_promo_code(self):

        """ Использование промокода """

        try:
            # Проверка и нажатие на кнопку
            value = self.check_and_click_checkbox(self.locator_promo_code_radio_button, 'aria-selected', 'true')

        except:
            # На случай если промокод выбран, но по умолчанию имеет значение aria-selected = false """
            self.click_element(self.locator_bonus_radio_button)
            value = self.check_and_click_checkbox(self.locator_promo_code_radio_button, 'aria-selected', 'true')

        print("___Click Checkbox 'Промокод'. Status before click: " + value[0] + "." + " Status after click: "
              + value[1] + "." + " Check PASSED")

    def click_apply_button(self):

        """  Клик по кнопке - Применить. """

        self.click_element(self.locator_apply_button)
        print("___Click Button 'Применить'")

    # Methods

    def add_contact_information(self):

        """ Заполнение раздела 'Контактная информация """

        # self.load_cookies('order_products_1')
        self.input_first_name()  # Ввод в поле Имя
        self.input_last_name()  # Ввод в поле Фамилия
        self.input_phone()  # Ввод в поле Телефон
        self.input_email()  # Ввод в поле Электронная почта
        self.screenshot('add_contact_information')  # Снимок экрана

    def select_self_delivery_method(self):

        """ Выбор способа доставки - Самовывоз. Проверка и нажатие на чек-бокс Самовывоз. """

        self.scroll_browser(0, 600)
        value = self.check_and_click_checkbox(self.locator_self_delivery_radio_button, 'checked', 'true')
        print("___Click Checkbox 'Самовывоз  по адресу  — 15 км от МКАД по М10'. Status before click: " +
              value[0] + "." + " Status after click: " + value[1] + "." + " Check PASSED")

    def select_legal_person_entity(self):

        """ Выбор Юридического лица. Проверка и нажатие на чек-бокс Юридическое лицо. """

        value = self.check_and_click_checkbox(self.locator_legal_person_radio_button, 'aria-selected', 'true')
        print("___Click Checkbox 'Юридическое лицо'. Status before click: " + value[0] + "." + " Status after click: " +
              value[1] + "." + " Check PASSED")

    def select_private_person_entity(self):

        """ Выбор Физического лица. Проверка и нажатие на чек-бокс Физическое лицо. """

        value = self.check_and_click_checkbox(self.locator_private_person_radio_button, 'aria-selected', 'true')
        print("___Click Checkbox 'Физическое лицо'. Status before click: " + value[0] + "." + " Status after click: " +
              value[1] + "." + " Check PASSED")

    def select_online_payment(self):

        """ Выбор способа оплаты - онлайн. Проверка и нажатие на кнопку Онлайн оплата """

        value = self.check_and_click_checkbox(self.locator_online_payment_radio_button, 'checked', 'true')
        print("___Click Checkbox 'Онлайн оплата'. Status before click: " + value[0] + "." + " Status after click: " +
              value[1] + "." + " Check PASSED")

    def select_promo_code(self):

        """ Добавление промокода. Проверка и нажатие на кнопку Промокод, ввод в поле Промокод. """

        self.click_radio_button_promo_code()
        self.input_promo_code()
