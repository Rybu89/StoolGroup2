from base.base_class import Base


class Main_page(Base):

    def __init__(self):
        super().__init__()

    # Test data

    url = 'https://stoolgroup.ru'


    # Locators

    locator_tables_button = ['xpath', '//a[@data-title="Столы"]']


    # Actions

    def click_tables_button(self):
        self.get_clikable_element(self.locator_tables_button).click()
        print("___Click Button 'Столы'")
        self.screenshot('tables_page')


    # Methods

    def click_and_check_tables_button(self):
        self.click_tables_button()