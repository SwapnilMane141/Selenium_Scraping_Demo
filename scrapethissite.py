from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from selenium.webdriver.common.by import By
import csv

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.scrapethissite.com/pages/ajax-javascript/#")

time.sleep(5)

year_elements = driver.find_elements(By.XPATH, "//a[@class='year-link']")

data = []

for each_year in year_elements:
    each_year.click()
    time.sleep(5)

    movie_names = driver.find_elements(By.XPATH, "//td[@class='film-title']")
    nominations = driver.find_elements(By.XPATH, "//td[@class='film-nominations']")
    filmAwards = driver.find_elements(By.XPATH, "//td[@class='film-awards']")

    for each_movie, nomination_num, award_num in zip(movie_names, nominations, filmAwards):
        
        data.append([each_movie.text, nomination_num.text, award_num.text])

driver.close()

with open('movies_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Movie Name", "Nominations", "Awards"])
    writer.writerows(data)

print("Data should have been written by now")