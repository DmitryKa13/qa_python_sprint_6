import allure
from selenium import webdriver
from pages.base_page import BasePage
from pages.home_page import HomePageLocators
from helpers.urls import Urls
from helpers.locators import BaseLocators


class TestCheckRedirect:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка процесса перехода на страницу Дзен по нажатию на логотип Яндекс.')
    @allure.description('На странице заказа ищем логотип Яндекса, нажимаем на него, и проверяем, '
                        'что выполнен переход на страницу Дзен.')
    def test_click_to_yandex_logo(self):

        start_page = BasePage(self.driver)
        start_page.open_url(Urls.order_url)

        start_page.scroll_and_click_on_element(BaseLocators.yandex_logo)
        start_page.switch_to_new_tab()
        start_page.wait_visibility_of_element(BaseLocators.dzen_page)

        assert Urls.dzen_url == start_page.get_current_url(), 'Страница Яндекс Дзен не открылась.'

    @allure.title('Проверка процесса перехода на главную страницу сервиса по нажатию на логотип Самокат.')
    @allure.description('На странице заказа ищем логотип Самокат, нажимаем на него, и проверяем, '
                        'что выполнен переход на главную страницу сервиса.')
    def test_click_to_scooter_logo(self):

        start_page = BasePage(self.driver)
        start_page.open_url(Urls.order_url)

        start_page.scroll_and_click_on_element(BaseLocators.scooter_logo)
        start_page.wait_visibility_of_element(HomePageLocators.title_of_home_page)

        assert Urls.home_url == start_page.get_current_url(), 'Домашняя страница сервиса аренды не отобразилась.'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
