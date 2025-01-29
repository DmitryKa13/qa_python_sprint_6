import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу {url}')
    def open_url(self, url):
        self.driver.get(url)

    @allure.step('Получаем URL активной страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Навигация до элемента страницы')
    def scroll_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*locator))

    @allure.step('Нажатие на элемент страницы')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def scroll_and_click_on_element(self, locator):
        self.scroll_to_element(locator)
        self.wait_clickability_of_element(locator)
        self.click_on_element(locator)

    @allure.step('Вводим значение в поле')
    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step('Эмуляция нажатия кнопки ESCAPE на клавиатуре')
    def send_escape(self):
        self.driver.send_keys(Keys.ESCAPE)

    @allure.step('Ожидаем отображения элемента на странице')
    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидаем пока элемент станет кликабельным')
    def wait_clickability_of_element(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step('Переключаемся на следующую вкладку в браузере')
    def switch_to_new_tab(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
