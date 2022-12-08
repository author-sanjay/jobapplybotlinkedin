
import os,random,time

from selenium.webdriver.chrome.service import Service
from  selenium import webdriver
from bs4 import BeautifulSoup
flagforeasyapply="&f_AL=true"

driverlink="/home/sanju/Downloads/chromedriver"
service=Service(executable_path=driverlink)
driver=webdriver.Chrome(service=service)

baseurl="https://www.linkedin.com/"
website=baseurl+"/uas/login?fromSignIn=true&trk=cold_join_sign_in"
links=[]
def jobapplylinked(preferedjobtitle,preferedlocation,flag):

    driver.get(website)
    time.sleep(3)
    elementID=driver.find_element(by="id",value='username')
    elementID.send_keys("sanjaykumar73189@gmail.com")
    elementID=driver.find_element(by="id",value='password')
    elementID.send_keys("TELL MY NAME")
    elementID.submit()
    for a in preferedjobtitle:
        x = a.replace(" ","%20").lower();
        for b in preferedlocation:
            y = b.replace(" ", "%20").lower();
            driver.get("https://www.linkedin.com/jobs/search/?keywords="+x+"&location="+y+"&f_TPR=r604800&f_AL=true");
            time.sleep(5)


            def getlinks(soup):
                ul=soup.find('div',{'class':'jobs-search-results-list'} )

                alllinks=ul.findAll('a')

                for all in alllinks:
                    temp=all['href'];
                    links.append("https://www.linkedin.com"+temp)
            getlinks(BeautifulSoup(driver.page_source))
            for i in links:
                print(i)

preferedjobtitle = ["Software Developer"]
    # , "React Js Developer", "Node Js Developer", "Full Stack Developer",
    #                     "Front End Developer", "BackEnd Developer"]
preferedlocation=["Delhi"]
# ,"Mumbai","Pune","United states","Germany","London"]
    # flag for remote
        # & f_WT = 2=remote
        # & f_WT = 1=onsite
        # & f_WT = 3= hybrid
flag="&f_WT=2"

jobapplylinked(preferedjobtitle,preferedlocation,flag)

for ele in  links:
    try:
        driver.get(ele)
        time.sleep(3)

        try:
            a=driver.find_element(by="xpath",value='/html/body/div[5]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div[3]/div/div/div/button')
            driver.execute_script("arguments[0].click();", a)
            try:
                b=driver.find_element(by="xpath",value='/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button')
                driver.execute_script("arguments[0].click();", b)
                try:
                    c=driver.find_element(by="xpath",value='/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]')
                    driver.execute_script("arguments[0].click();", c)
                    time.sleep(10)
                    try:
                        d=driver.find_element(by="xpath",value='/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[3]/button[2]')
                        driver.execute_script("arguments[0].click();", d)
                    except:
                        continue
                except:
                    continue
            except:
                continue

        except:
            continue

    except:
        continue
