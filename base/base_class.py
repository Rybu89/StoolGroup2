import datetime
import glob
import pickle
import time
import os

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base():

    options = webdriver.ChromeOptions()     # Создание объекта класса ChromeOptions
    # options.add_experimental_option("detach", True)     # Подключение опции - оставить браузер открытым в конце сессии
    options.add_argument("--incognito")     # Подключение опции - открыть браузер в режиме инкогнито
    options.add_argument("--disable-cache")     # Подключение опции - отменить загрузку кеша
    options.add_argument("--window-size=1920,1080")     # Подключение опции - открывать окно браузера в разрешении 1920х1080
    options.page_load_strategy = "eager"  # Подключение стратегии загрузки страницы - не ожидать полной отрисовки страниц
    # options.add_argument("--headless")      # Подключение опции - заппуск драйвера без графического отображения (безголовый режим)
    options.add_argument("--disable-blink-features=AutomationControlled")

    s = Service(executable_path="C:\\Users\\79531\\PycharmProjects\\resource\\new\\chromedriver.exe")
    browser = webdriver.Chrome(options=options, service=s)

    # Locators

    locator_ads_500_bonus = ['xpath', '//div[@id="popmechanic-form-60931"]/div[2]']      # ['xpath', '// div[@id="popmechanic-form-60931"]']       #['xpath', '//*[@id="popmechanic-container-60931"]/div[1]/div[1]']
    locator_ads_stoolgroup = ['xpath', '//div[@class="styles__CloseButtonContainer-sc-13lm8c2-0 lhDOjG"]']     #['xpath', '//div[@id="Calltouch-widget-container"]/div/div[2]']
    locator_all_ads = ['//*[@id="popmechanic-container-60931"]/div[1]/div[1]', '// *[contains(text(), "Нашли товар дешевле? Снизим цену!")]']        #'//div[@id="Calltouch-widget-container"]/div/div[2]'


    # Actions
    def get_clikable_element(self, element_locator):

        """ Метод получения кликабельного элемента по его локатору.
                Принимает:
                 element_locator - локатор элемента
        """

        return WebDriverWait(self.browser, 40).until(EC.element_to_be_clickable(element_locator))

    def get_present_element(self, element_locator):

        """ Метод получения элемента по его локатору.
                Принимает:
                 element_locator - локатор элемента
        """

        return WebDriverWait(self.browser, 40).until(EC.presence_of_element_located(element_locator))

    def click_element(self, element_locator):

        """ Метод нажатия на элемент.
            При открытии рекламы или долгой загрузке делает два клика в неактивную область возле значка корзины.
                Принимает:
                 element_locator - локатор элемента
        """

        try:
            WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((element_locator))).click()    # Нажатие на элемент

        except:     # Подаждать загрузку страницы и смахнуть рекламу
            time.sleep(2)

            clickable = self.browser.find_element("xpath", '//div[@id="cart_amount"]')
            ActionChains(self.browser)\
                .move_to_element(clickable)\
                .move_by_offset(20, 20)\
                .click() \
                .perform()

            time.sleep(2)

            clickable = self.browser.find_element("xpath", '//div[@id="cart_amount"]')
            ActionChains(self.browser) \
                .move_to_element(clickable) \
                .move_by_offset(20, 20) \
                .click() \
                .perform()

            WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((element_locator))).click()    # Повторное нажатие на элемент

    def get_value_text(self, element_locator):

        """ Метод получения значения атрибута "value" элемента в формате текста. При долгой загрузке страницы ожидает в течении 5 секунд.
                Принимает:
                 element_locator - локатор элемента
        """

        # try:
        return WebDriverWait(self.browser, 40).until(EC.element_to_be_clickable((element_locator))).get_attribute("value")      # Получение значения
        # except:
        #     time.sleep(5)       # Ожидание 5 секунд
        #     return WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((element_locator))).get_attribute("value")      # Повторное получение значения

    def get_text(self, element_locator):

        """ Метод получения текста содержащегося в элементе. При долгой загрузке страницы ожидает в течении 5 секунд.
                Принимает:
                 element_locator - локатор элемента
        """
        # try:
        return WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((element_locator))).text        # Получение текста
        # except:
        #     time.sleep(5)       # Ожидание 5 секунд
        #     return WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((element_locator))).text        # Повторное получения значения

    def open_page(self, url):

        """ Открытие страницы
        """

        # self.browser.maximize_window()
        self.browser.get(url)
        print('___Open page: ' + url)

    def check_page_title(self, title_value, title_locator):

        """ Метод проверки страницы по ключевому слову/заглавию.
                Принимает:
                 title_locator - локатор ключевого слова страницы
                 title_value - ожидаемое слово (Str)
        """

        result =WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable(title_locator)).text       # П
        assert title_value == result
        print('___Check page Passed: ' + result)

    def scroll_and_release(self, element_locator, step_scroll_x_y):

        """ Метод для скроллинга элементов на странице.
                Принимает:
                    element_locator - локатор элемента
                    step_scroll_x_y - шаг по оси Х, шаг по оси Y (Int)
        """

        element = WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable(element_locator))
        ActionChains(self.browser).click_and_hold(element).\
            move_by_offset(*step_scroll_x_y).release().perform()


    def scroll_browser(self, X, Y):

        """ Метод для скроллинга страницы браузера.
                Принимает:
                    step_x - шаг по оси Х
                    step_y - шаг по оси Y
        """

        self.browser.execute_script("window.scrollTo(" + str(X) + "," + str(Y) + ")")

    def check_and_click_dropdown_is_displayed(self, element_locator, element_locator_search):

        """ Метод для нажатия и проверки выпадающего списка. Проверяет выбран ли элемент, если нет, то выбирает его и проверяет статус.
                Принимает:
                   element_locator - локатор для выбора элемента
                   element_locator_search - локатор для проверки статуса элемента
                Вовзращает:
                   value_before - статус элемента до выбора (Boolean)
                   value_after - статус элемента после выбора (Boolean)
        """

        value_before = self.browser.find_element(*element_locator_search).is_displayed()
        if value_before == False:
            self.click_element(element_locator)
            time.sleep(2)
        value_after = self.get_present_element(element_locator_search).is_displayed()
        assert self.get_present_element(element_locator_search).is_displayed()
        return [value_before, value_after]


    def check_and_click_checkbox(self, input_locator, dynamic_attribute, selected_value_dynamic_atribut):

        """ Метод для нажатия и проверки чекбокса. Проверяет выбран ли элемент, если нет, то выбирает его и проверяет статус по изменению атрибута
                Принимает:
                   input_locator - локатор элемента
                   dynamic_attribute - проверяемый атрибут элемента (Str)
                   selected_value_dynamic_attribute - значение атрибута после выбора элемента (Str)
                Вовзращает:
                   value_before - статус атрибута до выбора (Str)
                   value_after - статус атрибута после выбора (Str)
        """

        value_before = str(self.browser.find_element(*input_locator).get_attribute(dynamic_attribute))
        if value_before not in selected_value_dynamic_atribut:
            self.click_element(input_locator)
        value_after = str(self.browser.find_element(*input_locator).get_attribute(dynamic_attribute))
        assert value_after == selected_value_dynamic_atribut
        return [value_before, value_after]

    def save_cookies(self, name_file_cookie):

        """ Метод для записи cookies.
                Принимает:
                   name_file_cookie - имя сохраняемого файла (Str)
        """
        print('\n Запись coockies')
        pickle.dump(self.browser.get_cookies(), open(os.getcwd() + '\\cookies\\' + f"{name_file_cookie}_cookies", "wb"))
        print('\n Coockies записаны')


    def load_cookies(self, name_file_cookie):

        """ Метод для загрузки cookies.
                Принимает:
                   name_file_cookie - имя загружаемого файла (Str)
        """

        print('\n Загрузка coockies')
        for cookie in pickle.load(open(os.getcwd() + '\\cookies\\' + f"{name_file_cookie}_cookies", "rb")):  #
            self.browser.add_cookie(cookie)
        self.browser.refresh()
        print('\n Coockies загружены')

    def screenshot(self, name):

        """ Метод для снимка экрана и сохранения файла в текущую дерикторию. Автоматически простовляет дату и время снимка в название файла.
                Принимает:
                   name - имя файла для сохранения (Str)
        """

        now_date = datetime.datetime.utcnow().strftime("%H.%M.%S.%d.%m.%Y")
        # pickle.dump(self.browser.get_screenshot_as_png(), open(os.getcwd() + '\\tests\\screenshots\\' f"{name}_screenshot" + now_date + '.png', "wb"))
        name_screenshot = os.getcwd() + '\\screenshots\\' + name + now_date + '.png'
        self.browser.save_screenshot(name_screenshot)

        print('___Screenshot')

    def deleting_all_screenshots(self):

        """ Метод для удаления всех файлов png из папки.
                Принимает:
                   answer - значения yes/YES/Yes для удаления файлов и любое другое для отмены (Str)
        """

        print('Удаление скриншотов')
        answer = input('Очистить папку с скриншотами? Yes/No: ')
        if answer == 'yes' or answer == 'YES' or answer == 'Yes' :
            path_for_del = os.getcwd() + '\\screenshots\\'
            file_for_del = "*.png"
            filelist = glob.glob(os.path.join(path_for_del, file_for_del))
        else:
            return
        for f in filelist:
            os.remove(f)


        print('Скриншоты удалены')

    def asser_word(self, word, result):

        """ Метод проверки страницы по ключевому слову.
                Принимает:
                 word - ключевое слово страницы
                 result - ожидаемое слово
        """

        value_word = word.text
        assert value_word == result
        print('Good value word: ' + value_word + ' PASSED')

    def move_to_element(self, element_locator):
        element = WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable(element_locator))
        ActionChains(self.browser).move_to_element(element).perform()
