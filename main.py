from bs4 import BeautifulSoup
import requests

url = "https://www.cvkeskus.ee/toopakkumised?op=search&search%5Bjob_salary%5D=3&ga_track=results&search%5Bcategories%5D%5B%5D=8&search%5Bkeyword%5D=&badge%5Bkeyword%5D=on&search%5Bexpires_days%5D=&search%5Bjob_lang%5D=&search%5Bsalary%5D="
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('article', attrs={'data-component':'jobad'})

for job in jobs:
    # Find the company name
    company_name = job.find('span', class_= 'job-company mr-5').text.replace(' ', '')
    # Find job description
    job_title = job.find('h2', class_='xl:text-xl').text.replace(' ', '')
    # Find link to job listing
    relative_job_url = job.find('a', class_= 'jobad-url')['href']
    complete_job_url = "https://www.cvkeskus.ee/" + relative_job_url
       
    print(f'''
    Company Name: {company_name}
    Job Title: {job_title}
    Job link: {complete_job_url}
    ''')