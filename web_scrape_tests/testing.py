#necessary imports
import requests
from bs4 import BeautifulSoup

#put the url in
url = "https://realpython.github.io/fake-jobs/"

#get the page out
page = requests.get(url)

#parse it using bs
soup = BeautifulSoup(page.content, "html.parser")

#search thru soup- id here is specific to div tag you're looking for 
results = soup.find(id="ResultsContainer")

print(results)

#every job posting is wrapped in a <div> element with the class card-content. 
#search thru results for those
job_elements = results.find_all("div", class_="card-content")


#here we pick out child elements for each i of prev results
# for i in job_elements:
#     title_element = i.find("h2", class_ = "title")
#     company_element = i.find("h3", class_ = "company")
#     location_element = i.find("p", class_ = "location")

#     #here we use .text to return only text aspect of html
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
#     print("\n")

#now filter for only specific jobs

# python_jobs = results.find_all(
#     "h2", string= lambda text: "python" in text.lower()
# )

# python_job_elements = [
#     h2_element.parent.parent.parent for h2_element in python_jobs
# ]

# #print(python_job_elements[0].text.strip())

# for i in python_job_elements:
#     title_element = i.find("h2", class_ = "title")
#     company_element = i.find("h3", class_ = "company")
#     location_element = i.find("p", class_ = "location")

#     #here we use .text to return only text aspect of html
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
#     print("\n")



