from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    ACCEPT_COOKIES_BUTTON = (By.CSS_SELECTOR, "button[class='base-button secondary normal']")
    WOMEN_SECTION = (By.CSS_SELECTOR, "a[title='Kobiety']")
    CLOTHES_SECTION = (By.CSS_SELECTOR, "a[title='ODZIEŻ']")
    POPUP_WINDOW = (By.CSS_SELECTOR, "button[class='button-icon close']")
    BLOUSES_AND_SHIRTS_SECTION = (By.XPATH, "//a[contains(text(),'Bluzki i koszule')]")
    SHIRTS_LOCATOR = (By.XPATH, "//a[contains(text(),'Koszule')]")
    OFFER_SECTION = (By.XPATH, "//span[contains(text(),'Oferta')]")
    NEW_CHECKBOX = (By.XPATH, "//div[contains(text(),'Nowość')]")
    SIZE_SECTION = (By.XPATH, "//span[contains(text(),'Rozmiar')]")
    TOP_DRESSING = (By.XPATH, "//div[contains(text(),'Górne części garderoby')]")
    SIZE_38 = (By.XPATH, "//span[contains(text(),'38')]")
    CONFIRM = (By.XPATH, "//span[contains(text(),'Wybieram')]")
    CONFIRM_WORKED = (By.XPATH, "//div[@class='filters']//span[contains(text(), '(1)')]")
    CLOTHES = (By.XPATH, "//li[@class='product'][1]//a")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(text(),'Dodaj do koszyka')]")
    SIZE_38_CHOOSER = (By.XPATH, "//tr[@class='row double']//td[contains(text(),'38')]")
    SIZE_38_CHOOSER_2 = (By.XPATH, "//tr[@data-test-value='38']")
    SIZE_M_CHOOSER = (By.XPATH, "//tr[@class='row double']//td[contains(text(),'M')]")

    SHOW_CART = (By.XPATH, "//button[contains(text(),'Pokaż koszyk')]")
    ERROR_MESSAGE = (By.XPATH, "//div[@class='base-alert-row messages-alert error']")

    PAGE_TITLE = (By.XPATH, "//h1[@class = 'title _heading-strong']")
    FILTERS = (By.XPATH, "//div[@class = 'base-tag filter-tag']")
    PRICE = (By.XPATH, "//div[@class='product-price price big inline']"
                       "//div[@class='final-price-wrapper text-sale']//div[@class='price']")
    PRICE_2 = (By.XPATH, "//div[@class='product-price price big inline']"
                         "//div[@class='final-price-wrapper text-tertiary']//div[@class = 'price']")
    PRICE_CONFIRMATION = (By.XPATH, "//div[@class = 'summary-row']//div[@class='price']")

    @staticmethod
    def filter_locator(filter_name):
        return By.XPATH, f"//div[contains(text(), '{filter_name}')]"


class CheckoutPageLocators(object):
    GO_TO_SHOP = (By.XPATH, "//button[contains(text(), 'Przejdź do kasy')]")
    CONTINUE_AS_GUEST = (By.XPATH, "//span[contains(text(), 'Kontynuuj jako gość')]")
    EMAIL_INPUT = (By.XPATH, "//input[@id='billing__email']")
    PHONE_INPUT = (By.XPATH, "//input[@id='billing__telephone']")
    NAME_INPUT = (By.XPATH, "//input[@id='billing__firstname']")
    SURNAME_INPUT = (By.XPATH, "//input[@id='billing__lastname']")
    STREET_INPUT = (By.XPATH, "//input[@id='billing__street-0']")
    HOUSE_NUMBER_INPUT = (By.XPATH, "//input[@id='billing__street-1']")
    POST_CODE_INPUT = (By.XPATH, "//input[@id='billing__postcode']")
    CITY_INPUT = (By.XPATH, "//input[@id='billing__city']")
    DHL = (By.XPATH, "//span[contains(text(), 'DHL')]")
    PAYU = (By.XPATH, "//span[contains(text(), 'Szybki przelew')]")
    TERMS = (By.XPATH, "//span[contains(text(), 'Oświadczam, że zapoznałem się z treścią')]")
    CONFIRM_PAYMENT = (By.XPATH, "//button[contains(text(), 'Zamawiam i płacę')]")

    PRICE_CONFIRMATION = (By.XPATH, "//div[@class = 'summary-row']//div[@class='price']")


class PayuPageLocators(object):
    PAY_WITH_CARD = (By.XPATH, "//a[@title='Płatność kartą']")
    CARD_DETAILS = (By.XPATH, "//a[@title='Podaj dane karty']")
    CARD_NUMBER_INPUT = (By.XPATH, "//input[@id='card-number']")
    CARD_DATE_INPUT = (By.XPATH, "//input[@id='card-date']")
    CARD_CVV_INPUT = (By.XPATH, "//input[@id='card-cvv']")
    SUBMIT_BUTTON = (By.XPATH, "//input[@type='submit']")
    CLOSE_AND_BACK = (By.XPATH, "//span[contains(text(), 'Zamknij i wróć')]")

    PRICE = (By.XPATH, "//em[@class = 'row']//div[2]")
    PAGE_HEADER = (By.XPATH, "//header[@class = 'row']//h1")
