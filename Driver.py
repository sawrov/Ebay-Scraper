from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Driver:
    def __init__(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.set_window_position(0,0)
        self.driver.set_window_size(1920, 1024)

    def loadurl(self,url):
        try:
            self.driver.get(url)
            # _=wait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='prcIsum']")))
            return True
        except:
            print("Invalid Url")
            self.terminate()
            quit()
    def terminate(self):
        self.driver.quit()



