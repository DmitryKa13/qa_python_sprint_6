from selenium.webdriver.common.by import By

class BaseLocators:

    # Яндекс лого на любой странице сервиса заказа
    yandex_logo = (By.XPATH, "//img[@alt='Yandex']")
    # Самокат лого на любой странице сервиса заказа
    scooter_logo = (By.XPATH, "//img[@alt='Scooter']")
    # Кнопка Найти на главной странице Яндекс Дзен
    dzen_page = (By.XPATH, ".//button[text()='Найти']")
