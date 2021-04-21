import requests
import json

host = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug_view'
path = '/annotations/heading/json?heading=Acid%20Value'
url = host + path

a = requests.get(url)
b = a.json()

for data in b["Annotations"]["Annotation"]:
    print(data)
    # print(data["LinkedRecords"][0]["CID"][0])