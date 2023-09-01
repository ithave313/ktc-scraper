from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to the downloaded web driver executable (e.g., chromedriver)
driver_path = '/path/to/chromedriver'

# Create a new Chrome browser instance
driver = webdriver.Chrome(executable_path=driver_path)

# Open the website
driver.get('https://keeptradecut.com/dynasty-rankings')

# Find the toggle element and click it
toggle_element = driver.find_element(By.ID, 'sf-toggle-toggle')
toggle_element.click()

# Wait for a moment to allow changes to take effect (optional)
# WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, 'loading-spinner')))

# Close the browser
driver.quit()
