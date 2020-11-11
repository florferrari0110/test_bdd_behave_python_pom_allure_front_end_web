from behave import *
from nose.tools import assert_equal, assert_true
from functions.Functions import Functions as Selenium
from pages.page_index import PageIndex
from pages.page_product import PageProduct

use_step_matcher("re")


class StepsDefinitions():

    @given('The user is in the main page (.*)')
    def step_impl(self, URL):
        Selenium.open_browser(self, URL=URL)

    @step('The user click on link (.*)')
    def step_impl(self,item ='Laptops'):
        PageIndex.click_link_categorie(self,item)

    @step('The user select the product (.*)')
    def step_impl(self, text="Sony vaio i5"):
        PageIndex.click_link_product(self, text)

    @step('The user click on add to cart')
    def step_impl(self):
        PageProduct.click_add_to_cart_button(self)

    @step('Assert the text of pop up is Product added')
    def step_impl(self, mensage='Product added'):
        text_of_popup = PageProduct.get_text_alert_popup(self)
        assert_equal(text_of_popup,mensage)

    @step('The user click on OK button')
    def step_impl(self):
        PageProduct.click_ok_button_alert(self)

    @then('Close the browser')
    def step_impl(self):
        Selenium.tearDown(self)

    @step('The user click on log in')
    def step_impl(self):
        PageIndex.click_log_in_link(self)

    @step('The user enter correct credentials')
    def step_impl(self):
        PageIndex.send_username_login(self, self.username)
        PageIndex.send_password_login(self, self.password)

    @step('The user click on sign up button')
    def step_impl(self):
        PageIndex.click_sign_up_button(self)

    @step('The user click on log in button')
    def step_impl(self):
        PageIndex.click_log_in_button(self)

    @step('Assert that the name of user is in the banner')
    def step_impl(self):
        text_of_link = PageIndex.get_name_user_of_link(self)
        assert_equal('Welcome '+self.username,text_of_link)

    @step('The user click on sing up')
    def step_impl(self):
        PageIndex.click_sign_up_link(self)
        print('Click on sign up ')

    @step('The user enters correct data')
    def step_impl(self):
        PageIndex.send_username_registered(self,self.username)
        PageIndex.send_password_registered(self,self.password)

    @step('The user click on log out')
    def step_impl(self):
        PageIndex.click_log_out_link(self)

    @step('Assert that the text of pop up is Sign up successful')
    def step_impl(self, mensage='Sign up successful.'):
        text_alert = PageIndex.get_text_alert_popup(self)
        assert_equal(text_alert,mensage)
        
    @step('Assert that the sign up link is visible')
    def step_impl(self, text='Sign up'):
        text_link = PageIndex.get_text_of_link_sing_up(self)
        assert_equal(text_link,text)

    @given('Open Browser Aplication')
    def open_browser(self):
        Selenium.open_browser(self)        