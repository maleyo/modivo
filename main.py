import unittest
from selenium import webdriver
import page
import HtmlTestRunner


class ModivoTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://modivo.pl/")

    def test_buying_specific_product(self):
        # Load the main page. The home page of Modivo PL.
        main_page = page.MainPage(self.driver)
        # Go to the list of clothes
        main_page.go_to_list_of_clothes()
        # Check if page title equal
        self.assertTrue(main_page.is_title_match('Bluzki i koszule damskie'), "Title doesn't match.")
        # Choose clothes from new offer
        main_page.choose_clothes_with_new_offer()
        # Check if filter is added
        self.assertTrue(main_page.is_filter_added("Nowość"), "Filter 'Nowość' not added.")
        # Choose clothes with 38 size
        main_page.choose_clothes_with_38_size()
        # Check if filter is added
        self.assertTrue(main_page.is_filter_added("Górne części garderoby 38"), "Filter 'Rozmiar' not added.")
        # Choose first cloth from list
        main_page.choose_first_clothes()
        # Get the cloth price, it will be used for future checking
        cloth_price = main_page.get_clothes_price()
        # Go to shopping cart
        main_page.go_to_shopping_cart()
        # Check if price in basket equal
        self.assertTrue(main_page.check_if_price_equal(cloth_price), "Price doesn't match")

        # Load checkout page
        checkout_page = page.CheckoutPage(self.driver)
        # Go to shop
        checkout_page.go_to_shop()
        # Check if pric equal
        checkout_page.check_if_price_equal(cloth_price)
        # Fill information about customer
        checkout_page.fill_information_about_customer()
        # Choose payment and confirm
        checkout_page.choose_payment_and_confirm()

        # Load Payu page
        payu_page = page.PayuPage(self.driver)
        # Check if price equal
        payu_page.check_if_price_equal(cloth_price)
        # Fill Card information
        payu_page.fill_card_options()
        # Check if authorization failed
        payu_page.is_authorization_failed()
        # Exit from payment
        payu_page.exit_from_payment()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Results'))
