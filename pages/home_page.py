from pages.base_page import BasePage
from helpers.urls import Urls
from selenium.webdriver.common.by import By


class HomePageLocators:

    # заголовок главной страницы
    title_of_home_page = (By.XPATH, "//div[@class='Home_Header__iJKdX']")
    # кнопка Заказать сверху страницы
    order_button_above = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    # кнопка Заказать снизу страницы
    order_button_below = (By.XPATH, "//button[@class='Button_Button__ra12g Button_UltraBig__UU3Lp']")


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Urls.home_url)
        self.locators = HomePageLocators()

    @staticmethod
    def generate_locator_to_question(text):
        return (By.XPATH, f"//div[text()='{text}']")

    @staticmethod
    def generate_locator_to_answer(text):
        return (By.XPATH, f"//div//p[text()='{text}']")

    # метод кликает на соответствующий вопрос из списка "Вопросы о важном"
    def click_on_question(self, question = ''):
        locator = self.generate_locator_to_question(question)
        self.scroll_to_element(locator)
        self.wait_clickability_of_element(locator)
        self.click_on_element(locator)

    # метод ожидания появления соответствующего ответа на выбранный вопрос
    def wait_for_load_answer(self, answer = ''):
        locator = self.generate_locator_to_answer(answer)
        return self.wait_visibility_of_element(locator)

    def click_on_order_button(self, locator = HomePageLocators.order_button_above):
        self.scroll_to_element(locator)
        self.wait_visibility_of_element(locator)
        self.click_on_element(locator)
