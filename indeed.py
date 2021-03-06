import requests
from bs4 import BeautifulSoup

LIMIT = 50
def get_last_page(url):    
  result = requests.get(f"{url}&limit={LIMIT}")
  soup= BeautifulSoup(result.text, "html.parser")
  try:
    pagination= soup.find("ul",{"class":"pagination-list"} )
    links= pagination.find_all("li")
    pages =[]
    for link in links[:-1]:
      pages.append(int(link.string))

    max_page = pages[-1]
    return min(5,max_page)
  except:
    return 0

def extract_job(html):
  title = html.find("h2",{"class":"title"}).find("a")["title"]
  company = html.find("div",{"class":"sjcl"}).find("span",{"class":"company"})
  company_anchor = company.find("a")    
  if company_anchor is not None:
    company = str(company_anchor.string).strip()
  else:
    company = str(company.string).strip()
  location = html.find("div",{"class":"recJobLoc"})["data-rc-loc"]
  job_id = html["data-jk"]
  return {'title':title, 'company':company, 'location':location, 'link':f"https://www.indeed.com/viewjob?jk={job_id}"}

def extract_jobs(last_page, url):
  jobs=[]
  for page in range(last_page):
    print(f"Scrapping page {page+1}")
    result = requests.get(f"{url}&start={page * LIMIT}")
    #print(result.status_code)  #200
    soup = BeautifulSoup(result.text,"html.parser")
    results = soup.find_all("div",{"class":"jobsearch-SerpJobCard"})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs
   
def get_jobs(word):    
  jobs =[]
  url = f"https://www.indeed.com/jobs?q={word}&limit={LIMIT}"
  last_page = get_last_page(url)
  if last_page > 0:
    jobs = extract_jobs(last_page,url)
  return jobs