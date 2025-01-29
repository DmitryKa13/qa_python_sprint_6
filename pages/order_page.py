import allure
from pages.base_page import BasePage
from helpers.urls import Urls
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class OrderPageLocators:

    # заголовок первой формы оформления заказа
    title_order_page_step1 = (By.XPATH, "//div[text()='Для кого самокат']")
    # поле Имя
    field_name = (By.XPATH, "//input[@placeholder='* Имя']")
    # поле Фамилия
    field_surname = (By.XPATH, "//input[@placeholder='* Фамилия']")
    # поле Адрес
    field_address = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    # поле Метро
    field_metro = (By.XPATH, "//input[@placeholder='* Станция метро']")
    # поле Телефон
    field_telephone = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    # кнопка Далее
    button_next = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    # заголовок второй формы оформления заказа
    title_order_page_step2 = (By.XPATH, "//div[text()='Про аренду']")
    # поле Дата
    field_date = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    # поле Срок
    field_period = (By.XPATH, "//div[text()='* Срок аренды']")
    # чекбокс цвет Черная жемчужина
    checkbox_black = (By.XPATH, "//label[@for='black']")
    # чекбокс цвет Серая исходность
    checkbox_grey = (By.XPATH, "//label[@for='grey']")
    # поле Комментарий
    field_comment = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    # кнопка Заказать
    button_order = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    # заголовок третьей формы оформления заказа
    title_order_page_step3 = (By.XPATH, "//div[text()='Хотите оформить заказ?']")
    # кнопка Да
    button_yes = (By.XPATH, "//div[@class='Order_Modal__YZ-d3']//button[text()='Да']")
    # заголовок окна подтверждения заказа
    title_order_confirmation = (By.XPATH, "//div[text()='Заказ оформлен']")

class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()

    @staticmethod
    def generate_locator_to_station_by_name(text):
        return (By.XPATH, f"//div[@class='select-search__select']/ul/li/button/div[text()='{text}']")

    @staticmethod
    def generate_locator_to_period(text):
        return (By.XPATH, f"//div[text()='{text}']")

    @staticmethod
    def generate_locator_to_scooter_color(text):
        locator = None
        if text == 'чёрный жемчуг':
            locator = OrderPageLocators.checkbox_black
        elif text == 'серая безысходность':
            locator = OrderPageLocators.checkbox_grey
        return locator

    @allure.step('Ожидаем первую форму оформления заказа')
    def wait_for_load_order_page_step1(self):
        self.wait_visibility_of_element(self.locators.title_order_page_step1)
        assert self.get_current_url() == Urls.order_url

    @allure.step('Заполняем первую форму заказа: Имя, Фамилия, Адрес, Метро, Телефон. Нажимаем кнопку Далее.')
    def fill_order_form_step1(self, name, surname, address, metro, telephone):
        self.send_keys_to_input(self.locators.field_name, name)
        self.send_keys_to_input(self.locators.field_surname, surname)
        self.send_keys_to_input(self.locators.field_address, address)

        self.click_on_element(self.locators.field_metro)
        self.scroll_and_click_on_element(self.generate_locator_to_station_by_name(metro))

        self.send_keys_to_input(self.locators.field_telephone, telephone)
        self.click_on_element(self.locators.button_next)

        assert self.wait_visibility_of_element(self.locators.title_order_page_step2)

    @allure.step('Заполняем вторую форму заказа: Дата, Срок, Цвет, Комментарий. Нажимаем кнопку Заказать.')
    def fill_order_form_step2(self, date, period, color, comment):
        self.send_keys_to_input(self.locators.field_date, date)
        self.send_keys_to_input(self.locators.field_date, Keys.ESCAPE)

        self.click_on_element(self.locators.field_period)
        self.scroll_and_click_on_element(self.generate_locator_to_period(period))

        self.click_on_element(self.generate_locator_to_scooter_color(color))
        self.send_keys_to_input(self.locators.field_comment, comment)
        self.click_on_element(self.locators.button_order)

        assert self.wait_visibility_of_element(self.locators.title_order_page_step3)

    @allure.step('На третьей форме заказа нажимаем кнопку ДАю')
    def fill_order_form_step3(self):
        self.click_on_element(self.locators.button_yes)

    @allure.step('Ожидаем окно с сообщением об успешном создании заказа.')
    def wait_for_load_order_confirmation(self):
        return self.wait_visibility_of_element(self.locators.title_order_confirmation)
