from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Initialize the webdriver
driver = webdriver.Chrome()
driver.get('https://www.gadgetbytenepal.com/category/mobile-price-in-nepal/')
time.sleep(5)

# Get the list of all the laptops
laptop_elements = driver.find_elements(By.XPATH, '/html/body/div[6]/div/div[3]/div/div/div/div[2]/div/div[1]')

# Extract text from the elements
laptop_data = []
for element in laptop_elements:
    laptop_data.append(element.text)

    print(laptop_data)

# Save the data to an Excel file using pandas
df = pd.DataFrame(laptop_data, columns=['Laptop Information'])
df.to_excel('laptop_data.xlsx', index=False)

# Close the driver
driver.quit()
