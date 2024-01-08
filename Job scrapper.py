import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import re
from selenium.webdriver.edge.service import Service
from selenium import webdriver
from random import randint
from selenium.webdriver.support import expected_conditions as EC
import csv

def get_driver(link):
    service = Service(executable_path='C:/Users/hardik/Downloads/edgedriver_win64/msedgedriver.exe')
    driver = webdriver.Edge(service=service)

    driver.get(link)
    
    content = driver.page_source
    
    soup = BeautifulSoup(content,'html.parser')
    driver.quit()
    return soup

def scraping(page):
    jobs = page.find_all("div", class_="job_seen_beacon")
    for job in jobs:

        company_name = job.find("span", class_="css-1x7z1ps eu4oa1w0").text

        company_location = job.find("div", class_="css-t4u72d eu4oa1w0").text

        salary=None
        try:
            salary = job.find("div", class_="metadata salary-snippet-container").text
            print("Original salary text:", salary)
           # cleaned_str = re.sub(r'[^\d$.,]', '', salary)
        except:
            salary = None

            
        job_title = job.find("a", class_="jcs-JobTitle css-jspxzf eu4oa1w0").text

        link_tag = job.find("a", class_="jcs-JobTitle css-jspxzf eu4oa1w0")
        link_half = link_tag["href"]
        base_url = "https://in.indeed.com"
        full_url = f"{base_url}{link_half}"

        job_info = {
            "job_title" : job_title,
            "salary" : salary,
            "company_name" : company_name,
            "company_location" : company_location,
            "link" : full_url
        }
        job_list.append(job_info)
        
job_list = []

#put number of pages * 10 in place of the second int in for
for i in range(0,500,10):
    page_html = get_driver(f"https://in.indeed.com/jobs?q=Python+Developer&l=Gurgaon%2C+Haryana&radius=50&start={i}&vjk=74df27615b32ca3c")
    scraping(page_html)

df = pd.DataFrame(job_list)
df.to_csv("jobs_indeed_python_developer.csv")