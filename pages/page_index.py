from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from functions.Functions import Functions
from selenium.webdriver.common.alert import Alert

class PageIndex(Functions):
  
    def click_sign_up_link(self):
        self.link_sign_up = (By.XPATH, '//*[@id="signin2"]')
        sign_up = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.link_sign_up))
        sign_up.click()

    def click_log_in_link(self):
        self.link_log_in = (By.XPATH, '//*[@id="login2"]')
        link_log_in = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.link_log_in))
        link_log_in.click()

    def send_username_registered(self,text):
        self.box_username_registered = (By.XPATH, '//*[@id="sign-username"]')
        box_username = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.box_username_registered))
        box_username.send_keys(text)

    def send_password_registered(self,text):
        self.box_password_registered = (By.XPATH, '//*[@id="sign-password"]')
        box_password = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.box_password_registered))
        box_password.send_keys(text)

    def send_username_login(self,text):
        self.box_username_login = (By.XPATH, '//*[@id="loginusername"]')
        send_username_login = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.box_username_login))
        send_username_login.send_keys(text)

    def send_password_login(self,text):
        self.box_password_login = (By.XPATH, '//*[@id="loginpassword"]')
        send_password_login = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.box_password_login))
        send_password_login.send_keys(text)

    def click_log_in_button(self):
        self.button_log_in = (By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
        click_log_in_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.button_log_in))
        click_log_in_button.click()

    def click_sign_up_button(self):
        self.button_sign_up = (By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]')
        button_sign = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.button_sign_up))
        button_sign.click()

    def get_text_of_link_sing_up(self):
        self.link_sign = (By.XPATH, '//*[@id="signin2"]')
        sign_up  = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.link_sign))
        texto = sign_up .text
        return texto    

    def get_name_user_of_link(self):
        self.link_name_user = (By.XPATH, '//*[@id="nameofuser"]')
        name_user = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.link_name_user))
        name = name_user.text
        return name
    
    def click_log_out_link(self):
        self.link_log_out = (By.XPATH, '//*[@id="logout2"]')
        link_log = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.link_log_out))
        link_log.click()

    def get_text_alert_popup(self):
        alerta = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        texto = alerta.text
        return texto

    def click_ok_button_alert(self):
        element =  WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        element.accept()

    def click_link_categorie(self,text):
        self.link_item = (By.LINK_TEXT, text)
        link_item = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.link_item))
        link_item.click()

    def click_link_product(self,text):
        self.link_product =  (By.LINK_TEXT, text)
        link_product = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.link_product))
        link_product.click()