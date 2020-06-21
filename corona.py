from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os
import time
import csv
from urllib.request import urlopen
from urllib.parse import quote_plus



path = os.getcwd() + "/chromedriver.exe"
driver = webdriver.Chrome(path)
title = []
road = []

try :
    driver.get("http://www.seoul.go.kr/coronaV/coronaStatus.do?menu_code=01#route_page_top")
    time.sleep(1)

    element = driver.find_element_by_class_name("move-tab")
    element.click()


    for i in range(3) :
        driver.implicitly_wait(10)
        time.sleep(5)

        html = driver.page_source
        bs = BeautifulSoup(html, "html.parser")

        conts = bs.findAll("div", class_ = "status-confirm")[3]
        


         


        for c in conts.findAll("td", class_ = "tdl") :
            print(c.text)
            road.append(c.text)
            
        ele = driver.find_elements_by_xpath('//*[@id="DataTables_Table_0_next"]')[1]
        driver.execute_script("arguments[0].click();", ele)
        driver.implicitly_wait(10)


            


        

        
        

finally :
    for t in title :
        if t.find("page") != -1 :
            print()
            print(t)
        else :
            print(t)
            

    driver.quit()


f = open('corona.csv', 'w', encoding = 'utf-8-sig', newline = '')
csvwriter = csv.writer(f)
for n in road :
    csvwriter.writerow(n)
f. close()

