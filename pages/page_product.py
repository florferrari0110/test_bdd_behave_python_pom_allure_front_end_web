from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from functions.Functions import Functions
from selenium.webdriver.common.alert import Alert

class PageProduct(Functions):

    def click_add_to_cart_button(self):
        self.button_add_to_cart = (By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')
        add_to_cart = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.button_add_to_cart))
        add_to_cart.click()

    def get_text_alert_popup(self):
        alerta = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        texto = alerta.text
        return texto

    def click_ok_button_alert(self):
        alerta = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
      # self.driver.switchTo().alert().accept()
        alerta.accept() 