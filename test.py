from selenium import webdriver
import chromedriver_autoinstaller


chromedriver_autoinstaller.install()

driver = webdriver.Chrome()  

# Go to the Google home page  
driver.get('https://github.com/JefferMarcelino')  

print(driver)
