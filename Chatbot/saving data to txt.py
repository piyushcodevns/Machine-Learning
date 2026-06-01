import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = "https://www.geeksforgeeks.org/machine-learning/machine-learning/"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
data = driver.find_element(By.CLASS_NAME, "text").text
df = pd.DataFrame(
    {"Topic": ["Machine Learning"], "Definition": [data], "Example": ["ML Example"]}
)
df.to_csv(r"e:\Machine Learning\Chatbot\ml.csv", index=False, encoding="utf-8")
print("CSV Saved Successfully!")
driver.quit()
