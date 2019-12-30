from selenium.webdriver.support.select import Select
import time
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options=Options()
options.headless=True
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://agmarknet.gov.in/PriceTrends/SA_Pri_Month.aspx')
id_box= driver.find_element_by_id('cphBody_Commodity_list')
select_id=Select(id_box)
select_id.select_by_visible_text('Cotton')
time.sleep(5)
for i in tqdm(range(2,20)):
    try:
        time.sleep(5)
        year_box= driver.find_element_by_id('cphBody_Year_list')
        select_year=Select(year_box)
        select_year.select_by_index(i)
        time.sleep(5)
    except: 
        continue
    print("CurrentYear",2000+i)
    for j in tqdm(range(1,13)):
        try:
            time.sleep(5)
            month_box= driver.find_element_by_id('cphBody_Month_list')
            select_month=Select(month_box)
            select_month.select_by_index(j)
            time.sleep(5)
            submit_button=driver.find_element_by_id('cphBody_But_Submit')
            submit_button.click()
            time.sleep(5)
            download_button=driver.find_element_by_id('cphBody_Button1')
            download_button.click()
            driver.back()
            time.sleep(5)
            id_box= driver.find_element_by_id('cphBody_Commodity_list')
            select_id=Select(id_box)
            select_id.select_by_visible_text('Cotton')
            time.sleep(5)
            year_box= driver.find_element_by_id('cphBody_Year_list')
            select_year=Select(year_box)
            select_year.select_by_index(i)
            print("Current_Month",j)
            time.sleep(10)
        except:
            continue
        

