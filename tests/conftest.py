import time

import pytest

from base.base_class import Base
from pages.cart_page import Cart_page
from pages.main_page import Main_page
from pages.tables_page import Tables_page

base = Base()
MP = Main_page()
TP = Tables_page()
CP = Cart_page()

@pytest.fixture(scope="module")
def from_module():
    print('\nНАЧАЛО')
    base.browser.delete_all_cookies()
    print('\n Test 1')

    yield
    # base.deleting_all_screenshots()
    # time.sleep(5)
    # base.browser.quit()
    print('\n КОНЕЦ')

@pytest.fixture()
def from_test_id_01():
    print('\n Start test_01')
    base.open_page(MP.url)
    MP.click_tables_button()

    yield
    base.save_cookies('select_products')
    print('\n Finish test_01')

@pytest.fixture()
def from_test_id_02():
    print('\n Start test_02')
    base.open_page("https://stoolgroup.ru/stoly/?features_hash=21-275_72-7048_81-14283_102-11927-83135-RUB_135-Y")
    base.load_cookies('select_products')

    yield
    print('\n Finish test_02')

@pytest.fixture()
def from_test_id_03():
    print('\n Start test_03')
    base.open_page("https://stoolgroup.ru/stoly/?features_hash=21-275_72-7048_81-14283_102-11927-83135-RUB_135-Y")
    base.load_cookies('order_products_1')
    TP.click_cart()
    CP.click_checkout_button()

    yield
    print('\n Finish test_03')
