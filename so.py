import requests
from bs4 import BeautifulSoup

def get_last_page(url):
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  try:
    pages = soup.find("div",{"class":"s-pagination"}).find_all("a")
    last_page =pages[-2].get_text(strip=True)
    last_page = int(last_page)
    return min(5,last_page)
  except:
    return 0

def extract_job(html):  
  title = html.find("h2").find("a")['title']
  company, location =html.find("h3").find_all("span", recursive =False)
  company = company.get_text(strip=True)
  location = location.get_text(strip=True)
  job_id =html.find("p",{"class":"mb0"}).find("a")["data-id"]
  return {'title':title, 'company':company, 'location':location, 'link':f"https://stackoverflow.com/jobs/{job_id}"}

def extract_jobs(last_page,url):
  jobs= []
  for page in range(last_page):    
    print(f"Scrapping page {page+1}")      
    result = requests.get(f"{url}&pg={page+1}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find("div",{"class":"listResults"}).find_all("div",{"class":"-job"})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs

def get_jobs(word):
  jobs =[]
  url = f"https://stackoverflow.com/jobs?q={word}"
  last_page = get_last_page(url)
  if last_page > 0:
    jobs = extract_jobs(last_page, url)
  return jobs
