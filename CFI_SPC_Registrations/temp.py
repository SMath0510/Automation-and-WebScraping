from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

# Set up Selenium webdriver
def launchBrowser():
   driver = webdriver.Chrome()
   CCCpath = f'file:///C:/Users/Admin/Desktop/Projects/Automation%20&%20Hashing/CFI_SPC_Registrations/Centre%20For%20Innovation%20_%20IIT%20Madras%20CCC.mhtml'
   CCpath = f'file:///C:/Users/Admin/Desktop/Projects/Automation%20&%20Hashing/CFI_SPC_Registrations/Centre%20For%20Innovation%20_%20IIT%20Madras%20CC.mhtml'
   driver.get(CCCpath)  # Replace with the URL of the login page

   print("Here")
   names = []
   emails = []
   numbers = []
    
   for i in range(1, 2830):
      path_name = "/html/body/div/div/div[1]/div[3]/div[3]/table/tbody/tr[" + str(i) + "]/th[2]"
      path_mail = "/html/body/div/div/div[1]/div[3]/div[3]/table/tbody/tr[" + str(i) + "]/th[3]"
      path_contact = "/html/body/div/div/div[1]/div[3]/div[3]/table/tbody/tr[" + str(i) + "]/th[5]"
      names.append(driver.find_element(By.XPATH, path_name).get_attribute("innerHTML"))
      emails.append(driver.find_element(By.XPATH, path_mail).get_attribute("innerHTML"))
      numbers.append(driver.find_element(By.XPATH, path_contact).get_attribute("innerHTML"))
      if(i % 100 == 0):
         print(f'Done with {i} registrations')
    
   print("Done 1")   
   workbook = openpyxl.Workbook()

   # Select the active sheet (first sheet by default)
   sheet = workbook.active

   for i in range(1, 2830):
      name = 'A' + str(i)
      email = 'B' + str(i)
      contact = 'C' + str(i)
      sheet[name] = names[i-1]
      sheet[email] = emails[i-1]
      sheet[contact] = numbers[i-1]

   # Save the workbook
   print("Done 2")
   workbook.save("ccc_registration_details.xlsx")
   while(True):
       pass

   
launchBrowser()