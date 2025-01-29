import allure
import pytest
from selenium import webdriver
from pages.home_page import HomePage, HomePageLocators
from pages.order_page import OrderPage


class TestCheckOrder:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize(
        'button, name, surname, address, metro, telephone, date, period, color, comment',
        [
            [
                HomePageLocators.order_button_above,
                'Дмитрий', 'Тест', 'Москва 42-72', 'Лубянка', '81234445566',
                '31.01.2025', 'сутки', 'серая безысходность', 'доставка до подъезда'
            ],

            [
                HomePageLocators.order_button_below,
                'Иван', 'Прог', 'Ижевск 34-65', 'Курская', '81234567890',
                '10.02.2025', 'четверо суток', 'чёрный жемчуг', 'комментарий'
            ]
        ]
    )
    @allure.title('Проверка процесса оформления заказа с правильными данными.')
    @allure.description('На главной странице заказа нажимаем кнопку Заказать, вводим все необходимые данные,'
                        'и оформляем заказ.')
    def test_do_order(self, button, name, surname, address, metro, telephone, date, period, color, comment):

        home_page = HomePage(self.driver)
        home_page.click_on_order_button()

        order_page = OrderPage(self.driver)
        order_page.wait_for_load_order_page_step1()

        order_page.fill_order_form_step1(name, surname, address, metro, telephone)
        order_page.fill_order_form_step2(date, period, color, comment)
        order_page.fill_order_form_step3()

        assert order_page.wait_for_load_order_confirmation(), 'Окно подтверждения успешного заказа не отображено'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
