from selenium.common import TimeoutException, NoSuchElementException

from locators import MainPageLocators, CheckoutPageLocators, PayuPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    def go_to_list_of_clothes(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.ACCEPT_COOKIES_BUTTON))
        element = self.driver.find_element(*MainPageLocators.ACCEPT_COOKIES_BUTTON)
        element.click()

        element = self.driver.find_element(*MainPageLocators.WOMEN_SECTION)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
        element.click()
        # Sleep 1 second for page reload
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.CLOTHES_SECTION))
        element = self.driver.find_element(*MainPageLocators.CLOTHES_SECTION)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
        element.click()

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.POPUP_WINDOW))
            element = self.driver.find_element(*MainPageLocators.POPUP_WINDOW)
            element.click()
        except TimeoutException:
            pass

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            MainPageLocators.BLOUSES_AND_SHIRTS_SECTION))
        element = self.driver.find_element(*MainPageLocators.BLOUSES_AND_SHIRTS_SECTION)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
        element.click()
        # Sleep 1 second for page reload
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.SHIRTS_LOCATOR))

    def is_title_match(self, title_name):
        # Sleep 1 second for title reload
        time.sleep(1)
        element = self.driver.find_element(*MainPageLocators.PAGE_TITLE)
        return title_name == element.text

    def choose_clothes_with_new_offer(self):
        # choose newest clothes
        element = self.driver.find_element(*MainPageLocators.OFFER_SECTION)
        element.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.NEW_CHECKBOX))
        element = self.driver.find_element(*MainPageLocators.NEW_CHECKBOX)
        element.click()
        element = self.driver.find_element(*MainPageLocators.CONFIRM)
        element.click()

    def is_filter_added(self, filter_name):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.
                                                                             filter_locator(filter_name)))
        elements = self.driver.find_elements(*MainPageLocators.FILTERS)
        filters = []
        for element in elements:
            filters.append(element.text)
        return filter_name in filters

    def choose_clothes_with_38_size(self):
        # choose 38 size
        element = self.driver.find_element(*MainPageLocators.SIZE_SECTION)
        element.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.TOP_DRESSING))
        element = self.driver.find_element(*MainPageLocators.TOP_DRESSING)
        element.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.SIZE_38))
        element = self.driver.find_element(*MainPageLocators.SIZE_38)
        element.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.CONFIRM))
        element = self.driver.find_element(*MainPageLocators.CONFIRM)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
        element.click()

    def choose_first_clothes(self):
        element = self.driver.find_element(*MainPageLocators.CLOTHES)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
        element.click()

    def get_clothes_price(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.PRICE))
            element = self.driver.find_element(*MainPageLocators.PRICE)
        except (NoSuchElementException, TimeoutException):
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.PRICE_2))
            element = self.driver.find_element(*MainPageLocators.PRICE_2)
        return element.text.replace(' ', '')

    def go_to_shopping_cart(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.ADD_TO_CART_BUTTON))
        element = self.driver.find_element(*MainPageLocators.ADD_TO_CART_BUTTON)
        element.click()
        # Sleep 1 second for reload page
        time.sleep(1)
        try:
            try:
                element = self.driver.find_element(*MainPageLocators.SIZE_38_CHOOSER)
                element.click()
            except NoSuchElementException:
                element = self.driver.find_element(*MainPageLocators.SIZE_38_CHOOSER_2)
                element.click()
        except NoSuchElementException:
            element = self.driver.find_element(*MainPageLocators.SIZE_M_CHOOSER)
            element.click()
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.SHOW_CART))
        except TimeoutException:
            try:
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.ERROR_MESSAGE))
                raise TimeoutException("Can't add to cart. The error message appears.")
            except NoSuchElementException:
                raise Exception("Something goes wrong.")

        element = self.driver.find_element(*MainPageLocators.SHOW_CART)
        element.click()

    def check_if_price_equal(self, price):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.PRICE_CONFIRMATION))
        element = self.driver.find_element(*MainPageLocators.PRICE_CONFIRMATION)
        return element.text.replace(' ', '') == price


class CheckoutPage(BasePage):
    def go_to_shop(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CheckoutPageLocators.GO_TO_SHOP))
        element = self.driver.find_element(*CheckoutPageLocators.GO_TO_SHOP)
        element.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CheckoutPageLocators.CONTINUE_AS_GUEST))
        element = self.driver.find_element(*CheckoutPageLocators.CONTINUE_AS_GUEST)
        element.click()

    def check_if_price_equal(self, price):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CheckoutPageLocators.PRICE_CONFIRMATION))
        element = self.driver.find_element(*CheckoutPageLocators.PRICE_CONFIRMATION)
        return element.text.replace(' ', '') == price

    def fill_information_about_customer(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CheckoutPageLocators.EMAIL_INPUT))
        element = self.driver.find_element(*CheckoutPageLocators.EMAIL_INPUT)
        element.send_keys("test@test.pl")
        element = self.driver.find_element(*CheckoutPageLocators.PHONE_INPUT)
        element.send_keys("123456789")
        element = self.driver.find_element(*CheckoutPageLocators.NAME_INPUT)
        element.send_keys("Tester")
        element = self.driver.find_element(*CheckoutPageLocators.SURNAME_INPUT)
        element.send_keys("Automatyczny")
        element = self.driver.find_element(*CheckoutPageLocators.STREET_INPUT)
        element.send_keys("Mickiewicza")
        element = self.driver.find_element(*CheckoutPageLocators.HOUSE_NUMBER_INPUT)
        element.send_keys("5")
        element = self.driver.find_element(*CheckoutPageLocators.POST_CODE_INPUT)
        element.send_keys("51-503")
        element = self.driver.find_element(*CheckoutPageLocators.CITY_INPUT)
        element.send_keys("Wrocław")

    def choose_payment_and_confirm(self):
        element = self.driver.find_element(*CheckoutPageLocators.DHL)
        element.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CheckoutPageLocators.PAYU))
        # Sleep 5 second for page reload
        time.sleep(5)
        element = self.driver.find_element(*CheckoutPageLocators.PAYU)
        element.click()
        # Sleep 5 second for page reload
        time.sleep(5)
        element = self.driver.find_element(*CheckoutPageLocators.TERMS)
        element.click()
        element = self.driver.find_element(*CheckoutPageLocators.CONFIRM_PAYMENT)
        element.click()


class PayuPage(BasePage):
    def check_if_price_equal(self, price):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PayuPageLocators.PRICE))
        element = self.driver.find_element(*PayuPageLocators.PRICE)
        payu_page = element.text.replace('.', ',')
        payu_page = payu_page.replace(' ', '')
        return payu_page == price

    def fill_card_options(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PayuPageLocators.PAY_WITH_CARD))
        element = self.driver.find_element(*PayuPageLocators.PAY_WITH_CARD)
        element.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PayuPageLocators.CARD_DETAILS))
        element = self.driver.find_element(*PayuPageLocators.CARD_DETAILS)
        element.click()
        element = self.driver.find_element(*PayuPageLocators.CARD_NUMBER_INPUT)
        element.send_keys("4111 1111 1111 1111")
        element = self.driver.find_element(*PayuPageLocators.CARD_DATE_INPUT)
        element.send_keys("12/24")
        element = self.driver.find_element(*PayuPageLocators.CARD_CVV_INPUT)
        element.send_keys("111")
        element = self.driver.find_element(*PayuPageLocators.SUBMIT_BUTTON)
        element.click()

    def is_authorization_failed(self):
        # Sleep 1 second for page reload
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PayuPageLocators.PAGE_HEADER))
        element = self.driver.find_element(*PayuPageLocators.PAGE_HEADER)
        return "Brak autoryzacji" == element.text

    def exit_from_payment(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PayuPageLocators.CLOSE_AND_BACK))
        element = self.driver.find_element(*PayuPageLocators.CLOSE_AND_BACK)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))
        element.click()
