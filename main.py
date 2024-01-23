from bs4 import BeautifulSoup
import requests

url = "https://www.cvkeskus.ee/toopakkumised?op=search&search%5Bjob_salary%5D=3&ga_track=results&search%5Bcategories%5D%5B%5D=8&search%5Bkeyword%5D=&badge%5Bkeyword%5D=on&search%5Bexpires_days%5D=&search%5Bjob_lang%5D=&search%5Bsalary%5D="
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('article', attrs={'data-component':'jobad'})
# Find company names and job description
for job in jobs:
    company_name = job.find('span', class_= 'job-company mr-5').text.replace(' ', '')
    #jobadUrl = job.find('a', class_= 'jobad-url').text.replace(' ', '')
    jobDescription = job.find('h2', class_='xl:text-xl').text.replace(' ', '')

    print(f'''
    Company Name: {company_name}
    Job description: {jobDescription}
    ''')


