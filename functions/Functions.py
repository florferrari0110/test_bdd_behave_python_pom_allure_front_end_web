from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
from functions.Inicializar import Inicializar
import random
import string

class Functions(Inicializar):

       def open_browser(self, URL=Inicializar.URL, browser=Inicializar.BROWSER):
              options = ChromeOptions()
              options.add_argument('start-maximized')
              self.driver = webdriver.Chrome(chrome_options=options,
                                                 executable_path=Inicializar.basepath + "/drivers/chromedriver")
              self.driver.implicitly_wait(10)
              self.driver.get(URL)
              self.driver.maximize_window()
              self.windows = {'Principal': self.driver.window_handles[0]}
              return self.driver

       def tearDown(self):
              self.driver.quit()
