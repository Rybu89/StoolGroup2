from base.base_class import Base


class Main_page(Base):

    def __init__(self):
        super().__init__()

    # Test data

    url = 'https://stoolgroup.ru'

    # Locators

    locator_tables_button = ['xpath', '//a[@data-title="Столы"]']
    locator_tables_title = ['xpath', '//h1[@class="tp_h-2 mb-0" and contains(text(), "Столы")]']

    # Actions

    def click_tables_button(self):
        self.get_clickable_element(self.locator_tables_button).click()
        value_title = self.asser_word(self.locator_tables_title, "Столы")
        print("___Click Button 'Столы'. Page title after clicking: " + value_title + " PASSED")

    # Methods

    def click_and_check_tables_button(self):
        self.click_tables_button()
        self.screenshot('tables_page')
