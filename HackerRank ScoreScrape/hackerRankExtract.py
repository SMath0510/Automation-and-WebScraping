from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import openpyxl
import time

#Set up Selenium webdriver
def launchBrowser():
   driver = webdriver.Chrome()
   driver.get("https://www.hackerrank.com/contests/cs2710-lab2/leaderboard")  # Replace with the URL of the login page

   print("Here")
   roll_no = []
   score = []
   times = []
   path_button = "/html/body/div[2]/div[10]/div/div/section/div[4]/div[2]/div/a/div"
   driver.find_element(By.XPATH, path_button).click()
   
   time.sleep(3)
   path_clk100 = "/html/body/div[7]/div/input"
   driver.find_element(By.XPATH, path_clk100).send_keys("100")
   driver.find_element(By.XPATH, path_clk100).send_keys(Keys.ENTER)
    
   time.sleep(3)

   for i in range(1, 98):
      path_roll_no = f"/html/body/div[2]/div[10]/div/div/section/div[2]/div[2]/div[{i}]/div/div[2]/p/a"
      path_score = f"/html/body/div[2]/div[10]/div/div/section/div[2]/div[2]/div[{i}]/div/div[4]/p"
      path_time = f"/html/body/div[2]/div[10]/div/div/section/div[2]/div[2]/div[{i}]/div/div[5]/p"
    #   print(path_roll_no, path_score, path_time)
      roll_no.append(driver.find_element(By.XPATH, path_roll_no).get_attribute("innerText"))
      score.append(driver.find_element(By.XPATH, path_score).get_attribute("innerText"))
      times.append(driver.find_element(By.XPATH, path_time).get_attribute("innerText"))
      if(i % 10 == 0):
         print(f'Done with {i} registrations')
    
   print("Done 1")   
   workbook = openpyxl.Workbook()

#    Select the active sheet (first sheet by default)
   sheet = workbook.active

   for i in range(1, 98):
      roll_noX = 'A' + str(i)
      scoreX = 'B' + str(i)
      timeX = 'C' + str(i)
      sheet[roll_noX] = roll_no[i-1]
      sheet[scoreX] = score[i-1]
      sheet[timeX] = times[i-1]

   # Save the workbook
   print("Done 2")
   workbook.save("lab2_cs2700.xlsx")
   while(True):
       pass

   
launchBrowser()