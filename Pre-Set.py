import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


options = uc.ChromeOptions()
options.headless = False
driver = uc.Chrome(options=options)
time.sleep(1)