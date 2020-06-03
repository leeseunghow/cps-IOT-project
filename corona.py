from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os
import time

path = os.getcwd() + "/7th/chromedriver"
driver = webdriver.Chrome(path)
title = []

try :
    driver.get("http://www.seoul.go.kr/coronaV/coronaStatus.do?menu_code=01#route_page_top")
    time.sleep(1)

    element = driver.find_element_by_class_name("move-tab")
    element.click()

    html = driver.page_source
    bs = BeautifulSoup(html, "html.parser")

    temp = bs.find("div", class_ = "dataTables_paginate paging_simple_numbers")

    pages = temp.find_all("a")

    for page in pages :
        print(page.text)


    for i in range(9) : 
        time.sleep(1)

        html = driver.page_source
        bs = BeautifulSoup(html, "html.parser")

        conts = bs.find("div", class_ = "status-confirm").find_all("tr")

        title.append("page" + str(i + 1))
        for c in conts :
            title.append(c.find("td", class_ = "tdl").find_all("p").find("b", "span").text)
        
        

finally :
    for t in title :
        if t.find("page") != -1 :
            print()
            print(t)
        else :
            print(t)
            

    driver.quit()
