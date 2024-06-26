import requests
from bs4 import BeautifulSoup
import pandas as pd



url = "https://www.gridgain.com/resources/glossary/high-performance-computing?utm_feeditemid=&utm_device=c&utm_term=hpc&utm_source=google&utm_medium=ppc&utm_campaign=PAM+GridGain+Use+Cases+-+US+%26+Canada&hsa_cam=19930741562&hsa_grp=150571241489&hsa_mt=p&hsa_src=g&hsa_ad=653908591400&hsa_acc=1578237114&hsa_net=adwords&hsa_kw=hpc&hsa_tgt=kwd-109235563&hsa_ver=3&gad_source=1&gclid=CjwKCAjw-O6zBhASEiwAOHeGxRjNZxL3EeLAaG-E1AmKTjn8ENzrFjFRTfqyIWOZMgYTgiXPHibPqBoC-N0QAvD_BwE" 
html = requests.get(url)

s = BeautifulSoup(html.text, 'html.parser')
#print(s.prettify()) #(prints website html transcript (just for fun))
"""
results = s.find(id= 'block-gridgain2021-content') #allows us to search "block grid grain content" for the main body text
main_text = results.find('h3', class_ = 'mt-5')
for i in main_text:
    print(i.text)
"""
box = s.find('div', class_= 'col') #boxing in the content that we want to scrape

title =box.find('h3').get_text() # finds title section wihtin html

content1 = box.find('p').get_text() #finds text section under title within html


#print(title)
#print(content1)

def web_printer():
    for i in box: #loop to print all paragraphs
        print(i.text)

web_printer()
