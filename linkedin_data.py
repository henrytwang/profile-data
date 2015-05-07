# LinkedIn Scraper
from bs4 import BeautifulSoup
import mechanize
import json

def get_profile_json_data(profile_url):
    br = mechanize.Browser()
    br.set_handle_robots(False)   # ignore robots
    br.set_handle_refresh(False)  # can sometimes hang without this
    br.addheaders = [('User-agent', 'Firefox')]

    response = br.open(profile_url)
    page = response.read()

    soup = BeautifulSoup(page)
    employee_name = soup.find(class_="full-name").text

    schools = []
    companies = []

    background_education_rs = soup.find_all(id="background-education")
    for links in background_education_rs:
        school_tags = links.findAllNext("h4", {'class': 'summary'})
        for school in school_tags:
            schools.append(school.string)

    background_experience_rs = soup.find_all(id="background-experience")
    for links in background_experience_rs:
        company_tags = links.findAllNext("h5")
        for company in company_tags:
            company_name_tag = company.find('a', {'dir': 'auto'})
            if company_name_tag:
                companies.append(company_name_tag.string)

    dict_to_convert = {}
    dict_to_convert['name'] = employee_name
    dict_to_convert['schools'] = schools
    dict_to_convert['companies'] = companies

    json_data = json.dumps(dict_to_convert)
    return json_data
