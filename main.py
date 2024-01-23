from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://www.cvkeskus.ee/toopakkumised?op=search&search%5Bjob_salary%5D=3&ga_track=results&search%5Bcategories%5D%5B%5D=8&search%5Bkeyword%5D=&badge%5Bkeyword%5D=on&search%5Bexpires_days%5D=&search%5Bjob_lang%5D=&search%5Bsalary%5D=").text
soup = BeautifulSoup(html_text, 'lxml')
job = soup.find('article', attrs={'data-component':'jobad'})

company_name = job.find('span', class_= 'job-company mr-5').text.replace(' ', '')

skills = job.find()

print(company_name)