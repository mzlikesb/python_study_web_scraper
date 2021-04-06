import requests
from bs4 import BeautifulSoup

URL = "https://stackoverflow.com/jobs?q=python"

def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pagination = soup.find("div",{"class":"s-pagination"}).find_all("a")
  last_page =pagination[-3].find("span").string
  last_page = int(last_page)
  return last_page

def extract_job(html):  
  title = html.find("h2").find("a")['title']
  company, location =html.find("h3").find_all("span", recursive =False)
  company = company.get_text(strip=True)
  location = location.get_text(strip=True)
  job_id =html.find("p",{"class":"mb0"}).find("a")["data-id"]
  return {'title':title, 'company':company, 'location':location, 'link':f"https://stackoverflow.com/jobs/{job_id}"}

def extract_jobs(last_page):
  jobs= []
  for page in range(last_page):    
    print(f"Scrapping page {page+1}")      
    result = requests.get(URL+f"&pg={page+1}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find("div",{"class":"listResults"}).find_all("div",{"class":"-job"})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs

def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs
