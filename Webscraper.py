from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello_world_2')
def hello_world_2():
    return 'Data Detectives'

@app.route('/scrape')
def scrape():
    url = "https://www.gridgain.com/resources/glossary/high-performance-computing?utm_feeditemid=&utm_device=c&utm_term=hpc&utm_source=google&utm_medium=ppc&utm_campaign=PAM+GridGain+Use+Cases+-+US+%26+Canada&hsa_cam=19930741562&hsa_grp=150571241489&hsa_mt=p&hsa_src=g&hsa_ad=653908591400&hsa_acc=1578237114&hsa_net=adwords&hsa_kw=hpc&hsa_tgt=kwd-109235563&hsa_ver=3&gad_source=1&gclid=CjwKCAjw-O6zBhASEiwAOHeGxRjNZxL3EeLAaG-E1AmKTjn8ENzrFjFRTfqyIWOZMgYTgiXPHibPqBoC-N0QAvD_BwE"
    html = requests.get(url)

    s = BeautifulSoup(html.text, 'html.parser')
    box = s.find('div', class_='col')

    # Extracting the dynamic fields
    Title = box.find('h3').get_text()
    Content1 = box.find('p').get_text()

    # Static values
    resource_url_type = 'URL'
    language = 'en'
    cost = 'no'
    id_ = 'std'
    visible_to = ['public']
    expertise_level = 'Beginner'
    learning_outcome = 'Understand'
    learning_resource_type = 'free text'
    license_ = None
    Author_name = ['Grid Gain']
    key_words = None
    target_groups = ['Students', 'Researchers']
    start = None
    time = None
    rating = None

    scraped_data = {
        'Title': title,
        'Url': url,
        'Resource_URL_Type': resource_url_type,
        'Language': language,
        'Cost': cost,
        'id': id_,
        'visible_to': visible_to,
        'Authors': author_name,
        'Expertise_Level': expertise_level,
        'Keywords': key_words,
        'Learning_Outcome': learning_outcome,
        'Learning_Resource_Type': learning_resource_type,
        'License': license_,
        'Target_Group': target_groups,
        'Start_Datetime': start,
        'Duration': time,
        'Rating': rating
    }

    return jsonify(scraped_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
