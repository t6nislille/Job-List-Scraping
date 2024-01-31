from bs4 import BeautifulSoup
import requests
from datetime import datetime
import time

def extract_job_info(job):
    company_name = job.find('span', class_='job-company mr-5').text.strip()
    job_title = job.find('h2', class_='xl:text-xl').text.strip()
    relative_job_url = job.find('a', class_='jobad-url')['href']
    complete_job_url = "https://www.cvkeskus.ee/" + relative_job_url
    return company_name, job_title, complete_job_url

def find_jobs():
    url = "https://www.cvkeskus.ee/toopakkumised?op=search&search%5Bjob_salary%5D=3&ga_track=results&search%5Bcategories%5D%5B%5D=8&search%5Bkeyword%5D=&badge%5Bkeyword%5D=on&search%5Bexpires_days%5D=&search%5Bjob_lang%5D=&search%5Bsalary%5D="
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('article', attrs={'data-component':'jobad'})

    save.jobs(jobs)

def save_jobs(jobs):
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f'posts/all_jobs_{current_time}.text'

    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(f"Date: {current_time}\n")
        
        for index, job in enumerate(jobs, start=1):
            company_name, job_title, complete_job_url = extract_job_info(job)
            f.write(f'Job {index}\n')
            f.write(f'Company Name: {company_name}\n')
            f.write(f'Job Title: {job_title}\n')
            f.write(f'More Info: {complete_job_url}\n\n')

        print(f'File saved: {file_name}')

